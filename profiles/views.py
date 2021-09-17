# from gitpro.accounts.models import Profile, Repository
from django.shortcuts import render
# from accounts.models import Profile
from django.contrib.auth.models import User
from accounts.models import Profile
from accounts.models import Repository
from datetime import datetime


def show_profile(request, userid):
    all_members=User.objects.all()
    user = User.objects.get(id=userid)
    prof= Profile.objects.get(user_id=userid)
    repo = Repository.objects.filter(profile_id=userid)
    k=prof.last_update
    dt=datetime.strptime(k,"%Y-%m-%d %H:%M:%S.%f")
    args={'usertoshow':user,
            'repostoshow':repo,
            'profiletoshow':prof,
            'datetime':dt,
            'user':request.user,
            'all':all_members}
    return render(request, 'profiles.html',args)
