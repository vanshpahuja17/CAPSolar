from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15, default="First")
    email = models.EmailField(max_length=50, default="Email")
    contact = models.CharField(max_length=10, default="0123456789")
    password = models.CharField(max_length=250, default="Passwd")
    location = models.CharField(max_length=20, default="applicant")
    gender = models.CharField(max_length=20, default="applicant")
    date_of_creation = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    email = models.EmailField(max_length=50, default="Email")
    factor = models.CharField(max_length=50 , default="None")
    mailsent = models.CharField(max_length=10 , default="No")