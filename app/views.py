import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def start(request):
    return render(request,"authenticate/start.html")

def register(request):
    return render(request,'sign_up.html')

def login(request):
    return render(request,'log_in.html')

