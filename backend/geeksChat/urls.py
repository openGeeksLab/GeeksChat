from django.conf.urls import url, include
from django.contrib import admin

from graphene_django.views import GraphQLView
from push_notifications.api.rest_framework import GCMDeviceAuthorizedViewSet

from apps.chat.views import FacebookLogin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^device/gcm/?$', GCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_gcm_device'),
]
