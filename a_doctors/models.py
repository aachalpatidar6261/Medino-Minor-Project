from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    password=models.CharField(max_length=100)
    address=models.TextField()
    profile_pic=models.ImageField(upload_to="profile_pic/",default="")
    usertype=models.CharField(max_length=100,default="Patient")

    def __str__(self):
        return self.fname

class Appointment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateTimeField('%Y-%m-%d')
    subject=models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    email=models.EmailField()
    msg=models.TextField()

    def __str__(self):
        return self.email