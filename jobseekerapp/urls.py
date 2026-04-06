from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jobseeker_home'),
    path('addprofile/', views.addprofile, name='addprofile'),
    path('profilelist/', views.profilelist, name='profilelist'),
]
