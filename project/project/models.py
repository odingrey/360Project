from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', default='profile_images/default.jpg', blank=True)
	
	def __unicode__(self):
		return self.user.username
