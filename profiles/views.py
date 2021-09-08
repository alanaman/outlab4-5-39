from django.shortcuts import render

def show_profile(request):
    return render(request, 'profiles.html')
