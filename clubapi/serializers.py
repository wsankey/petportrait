from django.contrib.auth.models import User, Group
from models import Owner, Artist, Pet, Portrait
from rest_framework import serializers


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	confirm_password = serializers.CharField(write_only=True, required=False)

	class Meta:
		model = Owner
		fields = ('id', 'email', 'username', 'created_at', 'updated_at', 
					'first_name', 'last_name', 'password', 'confirm_password')

		read_only_fields = ('created_at', 'updated_at')

		def create(self, validated_data):
			return Owner.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.username = validated_data.get('username', instance.username)

			instance.save()

			password = validated_data.get('password', None)

			if password and confirm_password and password == confirm_password:
				instance.set_password(password)
				instance.save()

			update_session_auth_hash(self.context.get('request'), instance)

			return instance

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artist
		fields = ('email', 'username', 'first_name', 'last_name', 'is_admin', 'created_at', 'updated_ad')

class PetSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pet
		fields = ('name', 'description', 'owner', 'has_portrait')

class PortraitSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Portrait
		fields = ('url', 'style', 'description', 'sale_price', 'available', 'artist')