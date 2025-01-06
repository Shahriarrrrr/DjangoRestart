from django.urls import path
from student.views import *

urlpatterns = [
    path('all/', all_data, name='all_data'),
    path('single/', single_data, name='single_data'),
]
