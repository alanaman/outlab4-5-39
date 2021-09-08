from django.shortcuts import render

def show_explore(request):
    return render(request, 'explore.html')
