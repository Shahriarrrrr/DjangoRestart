from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'student/home.html')

#Using only id
# def profile(request,my_id):
#     id = my_id
#     return render(request, 'student/profile.html', {"number" : id})

#using only class
def profile(request,my_class,my_id):
    student = {'class': my_class , 'id' : my_id}
    return render(request, 'student/profile.html', student)
#using custom converter (year)

# def profile(request,year):
#     student = {'year': year}
#     return render(request, 'student/profile.html', student)