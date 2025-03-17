from django.shortcuts import render

def home(request):
    context = {'data': 'Hello I am a django developer. I am '
    'also currently studying CSE in United International University.'}
    return render(request, 'student/home.html', context)

