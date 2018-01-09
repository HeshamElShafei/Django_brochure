from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ClubSignUp(models.Model):
	name = models.CharField(max_length=250)
	number = models.IntegerField()
	club_name = models.CharField(max_length=250)
	membership = models.CharField(max_length=250, default='HomeClubMembership')
	option = models.CharField(max_length=250, default='Monthly')
