from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from requests.api import request

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Followers = models.IntegerField(default=0)
    # git2 = models.CharField(max_length=100,default='')



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        P=Profile.objects.create(user=instance)
        U=User.objects.get(id=P.user_id)
        # print(U.username)
        URL='https://api.github.com/users/'+str(U.username)
        response=requests.get(URL)
        dict=response.json()
        print(dict)
        print(dict['followers'])
        P.Followers = dict['followers']



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()