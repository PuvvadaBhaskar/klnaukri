from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='employee_home'),
    path('crud/', views.crud, name='crud'),
    path('crud_insert/', views.crud_insert, name='crud_insert'),
    path('read_employee/',views.read_employee,name='read_employee'),
    path('update/', views.update_employee, name='update_employee'),
    path('delete/', views.delete_employee, name='delete_employee'),

]
