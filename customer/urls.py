from django.urls import path
from django.conf.urls import include, url
from .views import ApiEndpoint

urlpatterns = [
    url('', ApiEndpoint.as_view()),  # an example resource endpoint
]
