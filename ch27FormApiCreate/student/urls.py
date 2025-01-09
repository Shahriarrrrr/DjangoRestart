from django.urls import path
from .views import registration,login

urlpatterns = [
    path('register/', registration, name='registration'),
    path('login/', login, name='login')
]
