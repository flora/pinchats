from flask import current_app, request, Response, Blueprint
from pinchats import db_session
from models import User
import datetime
import simplejson


pinchats_blueprint = Blueprint('pinchats', __name__)

@pinchats_blueprint.route('/user', methods=['PUT'])
def add_user():
    """ Creates a new user in the system.
    Inputs:
        name
        email
        frequency
        team_name
        role
        months_at_company
    Response:
        200 if created
        409 if email already exists

    """
    request_dict = request.get_json(force=True)
    new_user = User(name=request_dict.get("name"),
                    email=request_dict.get("email"),
                    frequency=request_dict.get("frequency"),
                    team_name=request_dict.get("team_name"),
                    role=request_dict.get("role"),
                    months_at_company=int(request_dict.get("months_at_company")),
                    last_scheduled=None,
                    date_joined=datetime.datetime.now(),
                    active=True)
    db_session.add(new_user)
    db_session.commit()
    return Response(response=simplejson.dumps({}), status=200, mimetype='application/json')

@pinchats_blueprint.route('/users/<string:email>', methods=['PUT'])
def update_user(email):
    """ Update user
    Inputs:
        fields to be updated with new values
    Response:
        200 if success
        400 if failed validation
        404 if email doesn't exist
    """
    request_dict = request.get_json(force=True)
    user = User.query.filter_by(email=email).first()
    non_existent_fields = {}
    status = 200
    for attr in request_dict:
        if hasattr(user, attr):
            setattr(user, attr, request_dict.get(attr))
        else:
            non_existent_fields[attr] = request_dict.get(attr)
            status = 400
    db_session.commit()
    return Response(response=simplejson.dumps(non_existent_fields), status=status, mimetype='application/json')

@pinchats_blueprint.route('/pinchats', methods=['PUT'])
def setup_pinchats():
    # get all the users to schedule
    users_to_schedule = _get_users_to_schedule()

    # create graph with the correct candidate set for each user
    G = {}
    for user in users_to_schedule:
        G[user] = _get_pinchat_candidates(user, users_to_schedule)

    # get maximum matching for the graph
    # This returns a map u -> v with the matching for each user.
    # Note: both u -> v and v -> u are present in the map
    maximum_matching = matching(G)

    # convert the returned matching into pinchat groups
    pinchat_groups = list(set([sorted(key, value) for key, value in maximum_matching.iteritems()]))

    # some people left out? randomly match them among themlselves
    remaining_users = [user for user in users_to_schedule if user not in maximum_matching]
    # in case of odd numer of people left, put last one in the first group
    if len(remaining_users) % 2 != 0:
        if len(pinchat_groups) > 0:
            pinchat_groups[0].append(remaining_users[-1])
        else:
            pinchat_groups = [[remaining_users[-1]]]
        remaining_users = remaining_users[:-1]
    # pair remaining amongst themselves
    index = 0
    while index < len(remaining_users) - 1:
        pinchat_groups.append([remaining_users[index], remaining_users[index+1])
        index += 2

    # send out emails
    for group in pinchat_groups:
        _send_email(group)

    # TODO: update user last_scheduled field
    return Response(response=simplejson.dumps({}), status=200, mimetype='application/json')

def _send_email(group):
    from_addr = 'pinchats@pinterest.com'
    to_addr_list = [user.email for user in group]
    subject = 'We have a new PinChat for you!'
    message = 'Hey! How about meeting your co-worker for a chat?'
    login = 'anshul@pinterest.com'
    password = 'vflaeybjgriqfabn'
    smtpserver='smtp.gmail.com:587'

    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

def _get_pinchat_candidates(user, users_to_schedule):
    # all other users are possible candidates right now
    return [candidate for candidate in users_to_schedule if candidate != user]

def _get_users_to_schedule():
    users = User.query.all()
    users_to_schedule = []
    wiggle_room = datetime.timedelta(hours=12)
    # add wiggle room to account for the time that the script might take to schedule PinChats
    scheduling_time = datetime.now() + wiggle_room
    for user in users:
        next_date = user.last_scheduled
        if user.frequency == '1w' and scheduling_time >= user.last_scheduled + datetime.timedelta(weeks=1):
            users_to_schedule.append(user)
        elif user.frequency == '2w' and scheduling_time >= user.last_scheduled + datetime.timedelta(weeks=2):
            users_to_schedule.append(user)
        elif user.frequency == '1m' and user.last_scheduled.month != scheduling_time.month:
            users_to_schedule.append(user)
        else:
            # ERROR!
            raise Exception('Unrecognized frequency value - {}, should be one of (1w, 2w, 1m)'
                            .format(user.frequency))
    return users_to_schedule
