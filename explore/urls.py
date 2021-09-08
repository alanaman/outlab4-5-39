from django.urls import path
from explore import views


urlpatterns = [
    path('explore/', views.show_explore, name='explore'),
]