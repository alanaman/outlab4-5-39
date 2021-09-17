from django.urls import path
from profiles import views


urlpatterns = [
    path('<str:userid>/', views.show_profile, name='profiles'),
]