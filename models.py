from django.db import models


class Student(models.Model):
     
    firstname=models.CharField(max_length=100) 
    lastname=models.CharField(max_length=100) 
    collegename=models.CharField(max_length=100) 
    year=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    interns=models.IntegerField()
    percentage=models.IntegerField()
    domain=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    email=models.CharField(max_length=100)

# Create your models here.
