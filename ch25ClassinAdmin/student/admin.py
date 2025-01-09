from django.contrib import admin
from student.models import Profile, Result
# Register your models here.


admin.site.register(Profile) #Wont see in Admin until you register
admin.site.register(Result)