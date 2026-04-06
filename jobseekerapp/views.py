from django.shortcuts import render, redirect

from .forms import *
def home(request):
    return render(request, 'jobseekerapp/jobseekerhomepage.html')

def addprofile(request):
    if request.method == 'POST':
        form = JobSeekerProfileForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profilelist')
    else:
        form = JobSeekerProfileForm()
    return render(request, 'jobseekerapp/addprofile.html',{'form':form})

def profilelist(request):
    profiles = JobSeekerProfile.objects.all()
    return render(request, 'jobseekerapp/profilelist.html',{'profiles':profiles})

