from django.contrib.auth.models import User
from django.db import models

class Pet(models.Model):

	name = models.CharField(max_length=32, unique=True)
	description = models.CharField(max_length=200)
	owner = models.ForeignKey(User)
	has_portrait = models.BooleanField(default=False)

	def __unicode__(self):
		return u'%s whose parent is %s %s' % (self.name, self.owner.first_name, self.owner.last_name)

class Portrait(models.Model):

	style = models.CharField(max_length=32, unique=True)
	description = models.CharField(max_length=200)
	sale_price = models.DecimalField(decimal_places=2, max_digits=5)
	available = mdoels.BooleanField(default=False)
	artist = models.ForeignKey(Artist)

	def __unicode__(self):
		return u'%s %s offers %s at %s' % (self.artist.first_name, self.artist.last_name, self.style, self.sale_price)