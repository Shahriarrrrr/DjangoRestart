from django.shortcuts import render
from .models import Profile

# Create your views here.
def all_data(req):
    all_students = Profile.objects.all()
    # print(all_students[0].name)
    return render(req, 'student/all.html', {'students': all_students})
def single_data(req):
    single_student = Profile.objects.get(pk=2)
    print(f"Bogo: {single_student.name}")
    return render(req, 'student/single.html', {'student': single_student})