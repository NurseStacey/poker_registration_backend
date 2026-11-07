from django.db import models
from django.utils import timezone

class VenueModel(models.Model):
    venue_name=models.CharField(max_length=100, default='')

class GameModel(models.Model):
    venue=models.ForeignKey(VenueModel, null=True, on_delete=models.PROTECT)
    event_date=models.DateField(default=timezone.now)
    event_time=models.CharField(max_length=10, null=True)
    event_title=models.CharField(max_length=100, default='')
    completed=models.BooleanField(default=False)
    

class RosterModel(models.Model):
    game=models.ForeignKey(GameModel, null=True, default=None, on_delete=models.PROTECT, related_name='game_roster')
    player=models.CharField(null=True, max_length=50, default='')
    place=models.IntegerField(default=0)
