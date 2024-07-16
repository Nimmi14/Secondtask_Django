from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile = models.FileField(upload_to='patient_pics/')
    line1 = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile = models.FileField(upload_to='doctor_pics/')
    experience = models.IntegerField(default=0)
    line1 = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    C_CHOICES = [
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Viral Fever', 'Viral Fever'),
        ('Diarrhea','Diarrhea'),
        ('Stomach Aches','Stomach Aches'),
        ('Headaches','Headaches'),
        ('others','others'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='blog_images/')
    category = models.CharField(max_length=50,choices=C_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.post_title