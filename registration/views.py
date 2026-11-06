from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class RegisterForGame(APIView):
    def post(self, request, *args, **kwargs):
        try:
            return Response({'status':'Preferences updated'}, status =status.HTTP_200_OK )  
        except Exception as e:
            print(e)
            return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )  

class VenueAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer=VenueSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status =status.HTTP_200_OK )   
        except Exception as e:
            print(e)
        
        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )  

    def get(self, request, *args, **kwargs):
        try:
            all_venues=VenueModel.objects.all()
            serializer=VenueSerializer(all_venues, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )      

class GameAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer=GameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status =status.HTTP_200_OK )   
        except Exception as e:
            print(e)
        
        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )

    def get(self, request, *args, **kwargs):
        try:
            all_games=GameModel.objects.all().order_by('-event_date')
            serializer=GameSerializerForRegistration(all_games, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )      

class GameForRegistrationAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:

            all_games=GameModel.objects.filter(completed=False)
            serializer=GameSerializerForRegistration(all_games, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )

class GameRegisrtationAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer=RosterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status =status.HTTP_200_OK )   
        except Exception as e:
            print(e)
        
        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )    

class RosterAPI(APIView):
    def get(self, request, id, *args, **kwargs):

        try:
            this_game=GameModel.objects.get(id=id)
            this_roster=RosterModel.objects.filter(game=this_game).order_by('player')
            serializer=RosterSerializer(this_roster, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
        
        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )

class RemovePlayerAPI(APIView):
    def post(self, request, id, *args, **kwargs):
        try:
            this_player=RosterModel.objects.get(id=id)
            this_player.delete()

            return Response({'status':'OK'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        
        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST ) 

class GameCompleteAPI(APIView): 
    def post(self, request, id, *args, **kwargs):
        try:
            this_game=GameModel.objects.get(id=id)
            this_game.completed=True
            this_game.save()

            return Response({'status':'OK'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        
        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )     

class UpdateRosterAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            for one_player in request.data['roster']:
                print(one_player)
                this_player=RosterModel.objects.get(id=one_player['id'])
                print(this_player)
                this_player.place=int(one_player['place'])
                this_player.save()

            return Response({'status':'OK'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        
        return Response({'status':'Problem'}, status =status.HTTP_400_BAD_REQUEST )               