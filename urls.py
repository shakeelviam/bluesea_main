"""
URL configuration for recruitment_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bluesea_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('jobs/', views.job_list, name='job_list'),  # Job listing page
    path('profile/', views.applicant_profile, name='applicant_profile'),  # Applicant profile page
    path('job-post/', views.job_post, name='job_post'),  # Specific job post page
    path('new-post/', views.new_post, name='new_post'),  # Page for posting a new job
    # ... include other URL patterns as needed
]


