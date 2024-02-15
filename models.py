from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True)
    # Additional fields like location, job requirements, salary, etc.

    def __str__(self):
        return self.title

class Applicant(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_jobs = models.ManyToManyField(Job)
    # Additional fields like education, experience, etc.

    def __str__(self):
        return self.full_name

    


