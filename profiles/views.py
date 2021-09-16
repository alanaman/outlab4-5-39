from django.shortcuts import render
from accounts.models import UserProfile
from django.contrib.auth.models import User


def show_profile(request, username):
    all_members=User.objects.all()
    args={'name':username, 'user':request.user, 'all':all_members}
    return render(request, 'profiles.html',args)
