from django.contrib.auth.models import User, Group
from django.shortcuts import render
from models import Owner, Artist, Pet, Portrait
from rest_framework import viewsets
from serializers import *

# Create your views here.
def index(request):
	uid = request.session.get('user')
	if uid is None:
		#main landing page
		return render(request, 'clubapi/index.html')

class UserViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all()
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class OwnerViewSet(viewsets.ModelViewSet):

	queryset = Owner.objects.all()
	serializer_class = OwnerSerializer

class ArtistViewSet(viewsets.ModelViewSet):

	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

class PetViewSet(viewsets.ModelViewSet):

	queryset = Pet.objects.all()
	serializer_class = PetSerializer

class PortraitViewSet(viewsets.ModelViewSet):

	queryset = Portrait.objects.all()
	serializer_class = PortraitSerializer