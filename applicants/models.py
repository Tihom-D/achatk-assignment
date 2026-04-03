from django.db import models

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    role = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    candidate_response = models.TextField(blank=True, null=True)

    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name