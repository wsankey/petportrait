from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db import models

class OwnerManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        owner = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        owner.set_password(password)
        owner.save()

        return owner

    def create_superuser(self, email, password, **kwargs):
        owner = self.create_user(email, password, **kwargs)

        owner.is_admin = True
        owner.save()

        return owner

class Owner(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)

	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)

	is_admin = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']


class Artist(models.Model):

	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)

	is_admin = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_ad= models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

class Pet(models.Model):

	name = models.CharField(max_length=32, unique=True)
	description = models.CharField(max_length=200)
	owner = models.ForeignKey(Owner)
	has_portrait = models.BooleanField(default=False)

	def __unicode__(self):
		return u'%s whose parent is %s %s' % (self.name, self.owner.first_name, self.owner.last_name)


class Portrait(models.Model):

	style = models.CharField(max_length=32, unique=True)
	description = models.CharField(max_length=200)
	sale_price = models.DecimalField(decimal_places=2, max_digits=5)
	available = models.BooleanField(default=False)
	artist = models.ForeignKey(Artist)

	def __unicode__(self):
		return u'%s %s offers %s at %s' % (self.artist.first_name, self.artist.last_name, self.style, self.sale_price)