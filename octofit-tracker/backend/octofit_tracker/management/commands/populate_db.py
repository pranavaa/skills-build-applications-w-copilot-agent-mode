from django.core.management.base import BaseCommand
from fitness.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', members=['thundergod@mhigh.edu', 'metalgeek@mhigh.edu']),
            Team(name='Gold Team', members=['zerocool@mhigh.edu', 'crashoverride@mhigh.edu', 'sleeptoken@mhigh.edu']),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user='thundergod@mhigh.edu', type='Cycling', duration=60, date='2025-04-08'),
            Activity(user='metalgeek@mhigh.edu', type='Crossfit', duration=120, date='2025-04-07'),
            Activity(user='zerocool@mhigh.edu', type='Running', duration=90, date='2025-04-06'),
            Activity(user='crashoverride@mhigh.edu', type='Strength', duration=30, date='2025-04-05'),
            Activity(user='sleeptoken@mhigh.edu', type='Swimming', duration=75, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team='Blue Team', points=200),
            Leaderboard(team='Gold Team', points=300),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Road cycling event training', duration=60),
            Workout(name='Crossfit', description='Crossfit competition training', duration=120),
            Workout(name='Running Training', description='Marathon training', duration=90),
            Workout(name='Strength Training', description='Strength training', duration=30),
            Workout(name='Swimming Training', description='Swimming competition training', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
