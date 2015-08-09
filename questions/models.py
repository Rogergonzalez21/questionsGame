from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=128)
    value = models.ForeignKey(values)

    def __unicode__(self):
        return self.name

class Values(models.Model):
	value = models.CharField(max_length=64)
	points = models.IntegerField(default=0)

	def __unicode__(self):
		return self.value