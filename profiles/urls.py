from django.urls import path
from profiles import views


urlpatterns = [
    path('profiles/', views.show_profile, name='profiles'),
]