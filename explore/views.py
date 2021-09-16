from django.shortcuts import render
from django.contrib.auth.models import User

def show_explore(request):
    all_members=User.objects.all()
    args={'user':request.user, 'all':all_members}
    return render(request, 'explore.html', args)
