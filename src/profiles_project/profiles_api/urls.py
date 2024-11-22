from django.urls import path

from .views import *


urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
]