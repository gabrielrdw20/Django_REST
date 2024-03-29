from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet, basename='profile')

urlpatterns = [
    path('hello-view/', views.Hello.as_view()),
    path('', include(router.urls))
]
