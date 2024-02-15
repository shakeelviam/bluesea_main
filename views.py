from django.shortcuts import render
from django.urls import path, include


def home(request):
    return render(request, 'home.html')

def job_list(request):
    return render(request, 'job_list.html')

def applicant_profile(request):
    return render(request, 'applicant_profile.html')

def job_post(request):
    return render(request, 'job_post.html')  # Ensure this template name matches your HTML file

def new_post(request):
    return render(request, 'new_post.html')  # Ensure this template name matches your HTML file
