from django.contrib import admin
from clubapi.models import Owner, Artist, Pet, Portrait

class OwnerAdmin(admin.ModelAdmin):

	list_display = ['id', 'username', 'first_name', 'last_name']

class ArtistAdmin(admin.ModelAdmin):

	list_display = ['id', 'username', 'first_name', 'last_name']

class PetAdmin(admin.ModelAdmin):


	list_display = ['id', 'name', 'description', 'owner']

class PortraitAdmin(admin.ModelAdmin):

	list_display = ['id', 'style', 'description', 'artist']

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Portrait, PortraitAdmin)
