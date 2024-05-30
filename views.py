from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegisterForm, PrayerRequestForm
from .models import PrayerRequest

def home(request):
    return render(request, 'prayers/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'prayers/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'prayers/profile.html')

@login_required
def prayer_request(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            prayer_request = form.save(commit=False)
            prayer_request.user = request.user
            prayer_request.save()
            return redirect('home')
    else:
        form = PrayerRequestForm()
    return render(request, 'prayers/prayer_request.html', {'form': form})
