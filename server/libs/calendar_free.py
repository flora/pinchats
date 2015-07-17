import iso8601
import datetime
import simplejson
import requests

CREDENTIALS_FILE = '/mnt/cal_credentials.json'

def get_access_token():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    with open(CREDENTIALS_FILE, 'r') as f:
        credentials_dict = simplejson.loads(f.read())
        p = {"grant_type": "refresh_token",
             "refresh_token": credentials_dict['refresh_token'],
             "client_id": credentials_dict['client_id'],
             "client_secret": credentials_dict['client_secret']}
        r = requests.post('https://www.googleapis.com/oauth2/v3/token', params=p)
        return r.json()['access_token']

def datetime_in_calendar(t_interval, list_times):
    for interval in list_times:
        start = iso8601.parse_date(interval['start']).replace(tzinfo=None)
        end = iso8601.parse_date(interval['end']).replace(tzinfo=None)
        if t_interval[0] >= start and t_interval[1] <= end:
            return True
    return False

def get_free_time(emails):
    token = get_access_token()
    calendar_ids = [{"id": email} for email in emails]
    start_time = datetime.datetime.now()
    # earliest coffee date at 10AM
    start_time = start_time.replace(hour=17, minute=0, second=0, microsecond=0)
    time_min = start_time + datetime.timedelta(weeks = 1)
    time_max = start_time + datetime.timedelta(weeks = 2)
    d = {
          "timeMin": time_min.isoformat("T") + "Z",
          "timeMax": time_max.isoformat("T") + "Z",
          "items": calendar_ids
    }
    response = requests.post('https://www.googleapis.com/calendar/v3/freeBusy',
                             headers={'Authorization': 'Bearer {}'.format(token), 'content-type': 'application/json'},
                             data=simplejson.dumps(d))
    # find the hour or half hour that both people are free
    # assume there are two people for now
    calendars = response.json()['calendars']
    possible_meeting_times = [time_min + datetime.timedelta(minutes=i) for i in xrange(0, 7*24*60, 30)]
    # filter out meeting times that are too early (before 10AM) or too late (past 4PM)
    possible_meeting_times = filter(lambda x: x.hour >= 17 and x.hour <= 23 and x.weekday() < 5, possible_meeting_times)
    for meeting_time in possible_meeting_times:
        meeting_end_time = meeting_time + datetime.timedelta(minutes=30)
        num_busy_calendars = filter(lambda email: datetime_in_calendar((meeting_time, meeting_end_time), calendars[email]['busy']), emails)
        if len(num_busy_calendars) == 0:
            return meeting_time, meeting_end_time
    return None, None
