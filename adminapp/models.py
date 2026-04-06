from django.contrib.admindocs.utils import ROLES
from django.db import models

# Create your models here.
class Useraccount(models.Model):
    ROLE_CHOICES = [
        ('employee','Employee'),
        ('jobseeker','JobSeeker'),
    ]
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    phone = models.IntegerField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.firstname

class StudentFeedback(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    course_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comments = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name