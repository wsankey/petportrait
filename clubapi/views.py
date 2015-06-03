from models import Owner, Artist, Pet, Portrait
from serializers import OwnerSerializer, ArtistSerializer, PetSerializer, PortraitSerializer
from django.shortcuts import render
from permissions import *

from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.
def index(request):
	title = "Pet Portrait"
	uid = request.session.get('owner')

	if uid is None:
		#main landing page
		return render(request, 'clubapi/index.html')

class OwnerViewSet(viewsets.ModelViewSet):
	lookup_field = 'username'
	queryset = Owner.objects.all()
	serializer_class = OwnerSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			Owner.objects.create_user(**serializer.validated_data)

			return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
		
		return Response({
			'status': 'Bad request',
			'message': 'Account could not be created with current data.'
			}, status=status.HTTP_400_BAD_REQUEST)

class ArtistViewSet(viewsets.ModelViewSet):

	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

class PetViewSet(viewsets.ModelViewSet):

	queryset = Pet.objects.all()
	serializer_class = PetSerializer

class PortraitViewSet(viewsets.ModelViewSet):

	queryset = Portrait.objects.all()
	serializer_class = PortraitSerializer

