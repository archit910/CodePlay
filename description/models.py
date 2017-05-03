from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Description(models.Model):
	algo = models.CharField(max_length=1000)
	descript = models.CharField(max_length=2000)
	spaceComplexity = models.CharField(max_length=1000)
	timeComlexity = models.CharField(max_length=1000)
	links = models.CharField(max_length=2000)
	def __unicode__(self):
		return self.algo