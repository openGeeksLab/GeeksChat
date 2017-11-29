from django.conf.urls import url, include
from django.contrib import admin

from graphene_django.views import GraphQLView

from apps.chat.views import FacebookLogin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
]
