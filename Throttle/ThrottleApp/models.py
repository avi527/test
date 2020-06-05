from django.db import models
from django.db.models import Model
import datetime
from django.utils import timezone

class User(models.Model):
	ids=models.CharField(max_length=9,primary_key = True)
	real_name=models.CharField(max_length=30)
	tz=models.CharField(max_length=30,default='Asia/Kolkata')
	def __str__(self):
		return self.ids

class UserActivity(models.Model):
	userid=models.ForeignKey(User, on_delete=models.CASCADE,related_name='activity_periods')
	start_time=models.DateTimeField(default=timezone.now)
	end_time=models.DateTimeField(default=timezone.now)

	
	
	

