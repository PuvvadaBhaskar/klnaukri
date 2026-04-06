from django import forms

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = Useraccount
        fields = ['firstname','lastname','email','phone','role','password']
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = ['student_name', 'student_email', 'course_name', 'faculty_name', 'rating', 'comments']