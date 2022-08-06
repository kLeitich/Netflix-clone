import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def start(request):
    return render(request,"authenticate/start.html")

