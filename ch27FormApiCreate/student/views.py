from django.shortcuts import render
from student.forms import Registration, Login

# Create your views here.

def registration(req):
    fm  = Registration()
    #fm = Registration(field_order=['email', 'city']) #REORDER IN HTML
    return render (req, 'students/registration.html', {'form': fm})

def login(req):
    #CLASS CUSTOMIZATION
    # fm  = Login(auto_id='my_%s') #Change default
    # fm  = Login(auto_id=True) #Change default
    # fm  = Login(auto_id=False) #Change default
    #Maybe Has another method search if needed

    #SUFFIX CUSTOMIZATION
    #fm  = Login(label_suffix='A') #EmailA
    # fm  = Login(label_suffix='') #Email

    #INITIAL VALUE
    #fm  = Login(initial={'email': "Please Enter Email", 'password': "Please enter Password"})
    fm  = Login() 

    return render (req, 'students/login.html', {'form': fm})
