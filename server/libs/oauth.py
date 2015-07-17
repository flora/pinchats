import logging
import urlparse

from django.http import HttpResponseRedirect

from auth_client import OAuth
from auth_client import OAuthException
from auth_client import SessionOauthHandler
import settings

oauth = OAuth(
    secret=settings.ADMIN_OAUTH_SECRET,
    key=settings.ADMIN_OAUTH_CLIENT_ID,
    callback_url=settings.ADMIN_OAUTH_CALLBACK,
    oauth_handler=SessionOauthHandler(expires_name='employee_expires', token_name='employee_tok')
)


def get_employee(request):
    if oauth.validate_token(session=request.session):
        return request.session.get('employee_ldap')
    else:
        logout(request)
    return None


def login(request, redirect_path=None):
    data = None
    if redirect_path:
        data = {'redirect_path': redirect_path}
    return HttpResponseRedirect(oauth.get_authorization_url(session=request.session, data=data))
