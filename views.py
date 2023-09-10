from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    sd1=Student()
    return render(request,'index.html')
def add(request):
    return render(request,'surveytwo.html')
def sub(request):
    return render(request,'surveythree.html')
