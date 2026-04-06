from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail

from .forms import UserForm, FeedbackForm
from .models import Useraccount

import requests
import pytz
import datetime


# ---------------- HOME ----------------
def home(request):
    return render(request, 'adminapp/projecthomepage.html')


# ---------------- PRINTER ----------------
def printer(request):
    user_input = ""
    if request.method == "POST":
        user_input = request.POST.get('klu')

    return render(request, 'adminapp/printer.html', {'klu': user_input})


# ---------------- TIMETABLE ----------------
def timetable(request):
    return render(request, 'adminapp/timetable.html')


# ---------------- TIMEZONE ----------------
def time1(request):
    current_time = None
    error = None

    if request.method == 'POST':
        klu = request.POST.get('klu')
        try:
            tz = pytz.timezone(klu)
            current_time = datetime.datetime.now(tz)
        except:
            error = "Invalid Timezone"

    return render(request, 'adminapp/time1.html', {
        'time': current_time,
        'error': error
    })


# ---------------- SIGNUP ----------------
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('admin_home')
    else:
        form = UserForm()

    return render(request, 'adminapp/signup.html', {'form': form})


# ---------------- WEATHER ----------------
def weather(request):
    weather_data = {}
    error_message = ""

    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "YOUR_API_KEY_HERE"   # 🔥 replace with env variable later

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()

        if "main" in response:
            weather_data = {
                "city": city,
                "temperature": response["main"]["temp"],
                "description": response["weather"][0]["description"],
                "humidity": response["main"]["humidity"]
            }
        else:
            error_message = "Wrong Input / No City Found"

    return render(request, "adminapp/weather.html", {
        "weather": weather_data,
        "error": error_message
    })


# ---------------- LOGIN ----------------
def user_login(request):   # renamed ✅
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Useraccount.objects.get(email=email)

            if check_password(password, user.password):
                request.session["user_email"] = user.email
                request.session["user_name"] = user.firstname
                return redirect('admin_home')
            else:
                error = "Invalid Password"

        except Useraccount.DoesNotExist:
            error = "User does not exist"

        return render(request, 'adminapp/login.html', {'error': error})

    return render(request, 'adminapp/login.html')


# ---------------- LOGOUT ----------------
def logout(request):
    request.session.flush()
    return redirect('login')


# ---------------- FEEDBACK ----------------
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save()

            send_mail(
                subject="Feedback Submitted Successfully",
                message=(
                    f"Dear {feedback.student_name},\n\n"
                    "Thank you for submitting feedback for your course at KL University.\n\n"
                    "Your response has been recorded successfully."
                ),
                from_email='your_email@gmail.com',
                recipient_list=[feedback.student_email],
                fail_silently=False
            )

            return render(request, "adminapp/success.html")

    else:
        form = FeedbackForm()

    return render(request, "adminapp/feedback_form.html", {"form": form})