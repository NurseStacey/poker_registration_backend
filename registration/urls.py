from django.urls import path,include
from .views import *

urlpatterns = [
    path('venues/', VenueAPI.as_view(), name='add_venue'),
    path('games/', GameAPI.as_view(), name='games'),    
    path('games-for-registration/', GameForRegistrationAPI.as_view(), name='games-for-registration'),
    path('sign-up/', GameRegisrtationAPI.as_view(), name='sign-up'),     
    path('get-roster/<int:id>/', RosterAPI.as_view(), name='sign-up'),
    path('update-roster/', UpdateRosterAPI.as_view(), name='update-roster'),  
    path('game-complete/<int:id>/', GameCompleteAPI.as_view(), name='game-complete'),
    path('remove-player/<int:id>', RemovePlayerAPI.as_view(), name='remove-player'),
]