from rest_framework import generics, permissions
from .serializers import TripSerializer, TripToggleCompleteSerializer
from travelCompanion_App.models import Trip
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate



class TripListCreate(generics.ListCreateAPIView):
    # ListAPIView requires two mandatory attributes, serializer_class and
    # queryset.
    # We specify TripSerializer which we have earlier implemented

    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(user=user).order_by('-created')
        
        
    def perform_create(self, serializer):
        #serializer holds a django model
        serializer.save(user=self.request.user)
        
        
               

class TripRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts
        return Trip.objects.filter(user=user)
        
        
        
        
class TripToggleComplete(generics.UpdateAPIView):
    serializer_class = TripToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(user=user)
    def perform_update(self,serializer):
        serializer.instance.completed=not(serializer.instance.completed)
        serializer.save()
        
        
        
        
# view for new user signup
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request) # data is a dictionary
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status=201)
        except IntegrityError:
            return JsonResponse({'error':'username taken. choose another username'}, status=400)  # api signup post request tested with Insomnia
            
            
            

# view for user login
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
        request, 
        username=data['username'], 
        password=data['password'])
    if user is None:
        return JsonResponse({'error':'unable to login. check username and password'},status=400)
    else: # return user token
        try:
            token = Token.objects.get(user=user)
        except: # if token not in db, create a new one
            token = Token.objects.create(user=user)
        return JsonResponse({'token':str(token)}, status=201)