from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet)
urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls))
]