from django.shortcuts import render
from .forms import Registration

# Create your views here.

def registration(req):
    fm = Registration()
    return render (req, 'student/registration.html', {'form': fm})
