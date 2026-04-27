"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.OctofitUserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'leaderboard', views.LeaderboardEntryViewSet, basename='leaderboardentry')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
