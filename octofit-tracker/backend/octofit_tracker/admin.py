from django.contrib import admin
from fitness.models import User, Team, Activity, Leaderboard, Workout

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)