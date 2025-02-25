from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect

# Create your views here.

def register(request):
    if request.method == "POST":
        #print(f'The token is : {request.POST['csrfmiddlewaretoken']}')
        form =  Registration(request.POST)
        if form.is_valid() :
            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])
            print(form.cleaned_data["password"])
            #form = Registration() it would show form is empty but same issue
            #return HttpResponseRedirect('/student/success')
            return HttpResponseRedirect('/student/register')
    else:
        form = Registration()
    return render(request, 'student/register.html', {'form' : form})


def reg_success(request):
    return render(request, 'student/success.html')