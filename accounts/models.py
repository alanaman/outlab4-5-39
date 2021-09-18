from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import date, datetime
import requests


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Followers = models.IntegerField(default=0)
    last_update = models.DateTimeField(auto_now_add=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        P=Profile.objects.create(user=instance)
        U=User.objects.get(id=P.user_id)
        URL='https://api.github.com/users/'+str(U.username)
        try:
            response=requests.get(URL)
            dict=response.json()
        except:
            dict={}
            dict['followers']=0
        finally:
            if (dict['message']=="Not Found"):
                dict['followers']=0
        P.Followers = dict['followers']
        instance.profile.save()

post_save.connect(create_user_profile, sender=User)

class Repository(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    star_count = models.IntegerField(default=0)
    owner = models.CharField(max_length=100,default='')

def create_repos(sender, instance, created, **kwargs):
    P=Profile.objects.get(user=instance)
    U=User.objects.get(id=P.user_id)
    URL='https://api.github.com/users/'+str(U.username)+'/repos'
    
    try:
        response=requests.get(URL)
        dict=response.json()
    except:
        dict={}
    finally:
        if (dict['message']=="Not Found"):
            dict=[]
    
    for repo in dict:
        QS=Repository.objects.filter(name=repo['name'],profile=instance)
        if not QS:
            R=Repository.objects.create(profile=instance)
            R.name=repo['name']
            R.star_count=repo['stargazers_count']
            R.owner=repo['owner']['login']
            R.save()

post_save.connect(create_repos, sender=User)

def update_user_profile(id):
    P=Profile.objects.get(user_id=id)
    U=User.objects.get(id=P.user_id)
    URL='https://api.github.com/users/'+str(U.username)
    try:
        response=requests.get(URL)
        dict=response.json()
    except:
        dict={}
        dict['followers']=0
    finally:
        if (dict['message']=="Not Found"):
            dict['followers']=0    
    P.Followers = dict['followers']
    P.last_update = datetime.now()
    P.save()

def update_repos(id):
    Repository.objects.filter(profile_id=id).delete()
    P=Profile.objects.get(user_id=id)
    U=User.objects.get(id=P.user_id)
    URL='https://api.github.com/users/'+str(U.username)+'/repos'
    try:
        response=requests.get(URL)
        dict=response.json()
    except:
        dict={}
    finally:
        if (dict['message']=="Not Found"):
            dict=[]
    for repo in dict:
        QS=Repository.objects.filter(name=repo['name'],profile_id=id)
        if not QS:
            R=Repository.objects.create(profile_id=id)
            R.name=repo['name']
            R.star_count=repo['stargazers_count']
            R.owner=repo['owner']['login']
            R.save()