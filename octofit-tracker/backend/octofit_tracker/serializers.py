from rest_framework import serializers
from .models import OctofitUser, Team, Activity, LeaderboardEntry, Workout


class OctofitUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctofitUser
        fields = ['id', 'name', 'email', 'team']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'members']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity', 'duration']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'team', 'points']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'suggested_for']
