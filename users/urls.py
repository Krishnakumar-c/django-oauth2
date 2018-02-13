from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework import routers
from django.http import HttpResponse
from django.conf.urls import include, url

from .views import UserViewSet, GroupViewSet

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
app_name = 'users'

urlpatterns = [
    url(r'^', include(router.urls)),
]
