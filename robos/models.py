from django.db import models

# Create your models here.


class Function(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self): # __unicode__ on Python 2
		return self.name


class Robot(models.Model):
    name = models.CharField(max_length=200)
    functions = models.ManyToManyField(Function)

    def __str__(self): # __unicode__ on Python 2
    	return self.name
