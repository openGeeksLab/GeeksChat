from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework.authentication import TokenAuthentication


class FacebookLogin(SocialLoginView):
    authentication_classes = (TokenAuthentication,)
    adapter_class = FacebookOAuth2Adapter
