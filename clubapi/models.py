from django.contrib.auth.models import User
from django.db import models

class Pet(models.Model):

	name = models.CharField(max_length=32, unique=True)
	description = models.CharField(max_length=200)
	owner = models.ForeignKey(User)
	has_portrait = models.BooleanField(default=False)

	def __unicode__(self):
		return u'%s whose parent is %s %s' % (self.name, self.owner.first_name, self.owner.last_name)