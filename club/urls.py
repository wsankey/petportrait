from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from clubapi.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'owner', OwnerViewSet)
router.register(r'artist', ArtistViewSet)
router.register(r'pet', PetViewSet)
router.register(r'portrait', PortraitViewSet)

urlpatterns = [
	url(r'^$', 'clubapi.views.index', name='home'),
	url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
