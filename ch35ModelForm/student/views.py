from django.shortcuts import render
from .form import Registration
from django.http import HttpResponseRedirect
from .models import Profile

# # Create your views here.

def register(request):
    if request.method == "POST":
        #print(f'The token is : {request.POST['csrfmiddlewaretoken']}')
        form =  Registration(request.POST)
        if form.is_valid() :
            nm = form.cleaned_data["name"]
            em = form.cleaned_data["email"]
            pw = form.cleaned_data["password"]
            cwp = form.cleaned_data["confirm_password"]
            phn = form.cleaned_data["phone"]


            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])
            print(form.cleaned_data["password"])
            print(form.cleaned_data["confirm_password"])
            print(form.cleaned_data["phone"])
            if pw == cwp:
                pr = Profile(name = nm, email = em, password = pw, phone = phn)
                pr.save()
                print("HOGA")
                return HttpResponseRedirect('/student/register')
            else:
                print("Password Doesn't Match")
                form = Registration()
    else:
        print("ERROR")
        form = Registration()
    return render(request, 'student/register.html', {'form' : form})


def reg_success(request):
    return render(request, 'student/success.html')