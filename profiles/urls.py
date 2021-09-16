from django.urls import path
from profiles import views


urlpatterns = [
    path('<str:username>/', views.show_profile, name='profiles'),
]