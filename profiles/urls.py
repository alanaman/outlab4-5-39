from django.urls import path
from profiles import views


urlpatterns = [
    path('<str:userid>/', views.show_profile, name='profiles'),
    path('<str:userid>/update', views.update_profile, name='update'),
]