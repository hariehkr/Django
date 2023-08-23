from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    #delete user , profile also get delete
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    #pillow should install, for image
    image = models.ImageField(default = 'profilepic.jpg',upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username