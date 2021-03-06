from django.db import models

# Create your models here.

class Values(models.Model):
	value = models.CharField(max_length=64)

	def __unicode__(self):
		return self.value


class Dificulty(models.Model):
	dificulty = models.CharField(max_length=64)

	def __unicode__(self):
		return self.dificulty
		
class Question(models.Model):
    question = models.CharField(max_length=128)
    dificulty = models.ForeignKey(Dificulty)
    value = models.ForeignKey(Values)


    def __unicode__(self):
        return self.question