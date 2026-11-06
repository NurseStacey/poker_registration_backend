from rest_framework import serializers
from .models import VenueModel,GameModel,RosterModel

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model=VenueModel
        fields='__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model=GameModel
        fields='__all__'

class GameSerializerForRegistration(serializers.ModelSerializer):
    button_title=serializers.SerializerMethodField()

    class Meta:
        model=GameModel
        fields=['id', 'button_title','completed']

    def get_button_title(self, obj):
        return '{}-{} - {} - {}'.format(obj.venue.venue_name, obj.event_title,obj.event_date.strftime('%m/%d'), obj.event_time)

class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model=RosterModel
        fields='__all__'