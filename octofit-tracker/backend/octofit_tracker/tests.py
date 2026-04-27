from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import OctofitUser, Team, Activity, LeaderboardEntry, Workout


class OctofitTrackerApiTests(APITestCase):
    def setUp(self):
        OctofitUser.objects.create(name='Superman', email='superman@dc.com', team='dc')
        Team.objects.create(name='dc', members=['Superman'])
        Activity.objects.create(user='Superman', activity='Flight', duration=60)
        LeaderboardEntry.objects.create(team='dc', points=140)
        Workout.objects.create(name='Strength Training', suggested_for=['Superman'])

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)

    def test_users_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_teams_list(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_activities_list(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_leaderboard_list(self):
        url = reverse('leaderboardentry-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_workouts_list(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
