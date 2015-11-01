from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Usuario(AbstractBaseUser):
	nome = models.CharField(u'Nome Completo', max_length=100)
	email = models.EmailField(u'E-mail', blank=False, unique=True)
	USERNAME_FIELD = 'email'

class Function(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self): # __unicode__ on Python 2
		return self.name


class Robot(models.Model):
    name = models.CharField(max_length=200)
    functions = models.ManyToManyField(Function)

    def __str__(self): # __unicode__ on Python 2
    	return self.name
