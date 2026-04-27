from django.db import models


class OctofitUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    duration = models.IntegerField()

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user} - {self.activity}"


class LeaderboardEntry(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.team}: {self.points}"


class Workout(models.Model):
    name = models.CharField(max_length=255)
    suggested_for = models.JSONField(default=list)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
