from flask import current_app, request, Response
from pinchats import app
from models import User
import datetime
import simplejson


@app.route('/user', methods=['PUT'])
def add_user():
    """ Creates a new user in the system.
    Inputs:
        name
        alias
        frequency
        team_name
        role
        months_at_company
    Response:
        200 if created
        409 if alias already exists

    """
    request_dict = request.get_json(force=True)
    new_user = User(request_dict.get("name"),
                    request_dict.get("alias"),
                    request_dict.get("frequency"),
                    request_dict.get("team_name"),
                    request_dict.get("role"),
                    request_dict.get("months_at_company"),
                    None,
                    datetime.datetime.now(),
                    True)
    db.session.add(new_user)
    db.session.commit()
    return Response(response=simplejson.dumps({}), status=200, mimetype='application/json')

@app.route('/users/<string:alias>', methods=['PUT'])
def update_user(alias):
    """ Update user
    Inputs:
        fields to be updated with new values
    Response:
        200 if success
        400 if failed validation
        404 if alias doesn't exist
    """
    request_dict = request.get_json(force=True)
    user = User.query.filter_by(alias=alias).first()
    non_existent_fields = {}
    status = 200
    for attr in request_dict:
        if hasattr(user, attr):
            setattr(user, attr, request_dict.get(attr))
        else:
            non_existent_fields[attr] = request_dict.get(attr)
            status = 400
    db.session.commit()
    return Response(response=simplejson.dumps(non_existent_fields), status=status, mimetype='application/json')

@app.route('/pinchats', methods=['PUT'])
def setup_pinchats():
    # get all the users to schedule
    users_to_schedule = _get_users_to_schedule()
    # TODO: bipartite matching
    # TODO: send out emails
    # TODO: update user last_scheduled field
    return Response(response=simplejson.dumps({}), status=200, mimetype='application/json')

def _get_users_to_schedule():
    users = User.query.all()
    users_to_schedule = []
    wiggle_room = datetime.timedelta(hours=12)
    for user in users:
        next_date = user.last_scheduled
        if user.frequency == '1w':
            next_date += datetime.timedelta(weeks=1)
        elif user.frequency == '2w':
            next_date += datetime.timedelta(weeks=2)
        elif user.frequency == '1m':
            # get current month
            current_month = datetime.datetime.now().month
            if (next_date + datetime.timedelta(weeks=4)).month == next_date.month:
                next_date += datetime.timedelta(weeks=5)
            else:
                next_date += datetime.timedelta(weeks=4)
        else:
            # ERROR!
            raise Exception()
        if next_date < datetime.datetime.now() - wiggle_room:
            # this user needs to be scheduled
            users_to_schedule.append((user, next_date))
    return users_to_schedule
