from django import forms

from .models import *


class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['name','qualification','hobbies','skills','address','profile_photo']
