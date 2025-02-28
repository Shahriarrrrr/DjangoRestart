from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from .models import Profile

# Create your views here.

def register(request):
    if request.method == "POST":
        #print(f'The token is : {request.POST['csrfmiddlewaretoken']}')
        form =  Registration(request.POST)
        if form.is_valid() :
            nm = form.cleaned_data["name"]
            em = form.cleaned_data["email"]
            pw = form.cleaned_data["password"]


            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])
            print(form.cleaned_data["password"])
            #form = Registration() it would show form is empty but same issue
            #return HttpResponseRedirect('/student/success'0)

            #Update Into Database
            User = Profile(id = 1) #I have hard coded but usually it will be found or passed
            User.delete()


            # #Update Into Database
            # User = Profile(id = 12, name= nm, email = em, password =pw)
            # User.save()

            # #Save Into Database
            # User = Profile(name= nm, email = em, password =pw)
            # User.save()
            return HttpResponseRedirect('/student/register')
    else:
        form = Registration()
    return render(request, 'student/register.html', {'form' : form})


def reg_success(request):
    return render(request, 'student/success.html')