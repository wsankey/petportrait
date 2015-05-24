from django.contrib.auth.models import User, Group
from models import Owner, Artist, Pet, Portrait
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Owner
		fields = ('url', 'first_name', 'username')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artist
		fields = ('url', 'first_name', 'username')

class PetSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pet
		fields = ('url', 'name', 'description', 'owner', 'has_portrait')

class PortraitSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Portrait
		fields = ('url', 'style', 'description', 'sale_price', 'available', 'artist')