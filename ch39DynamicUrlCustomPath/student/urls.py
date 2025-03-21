from django.urls import path, register_converter
from .views import home,profile
from student.converters import FourDigitYearConverter


register_converter(FourDigitYearConverter, 'yyyy')


urlpatterns = [
    path('', home , name = "home"),
    #path('profile/<int:my_id>', profile , name = "profile"),
    # path('profile/<slug:title>', profile , name = "profile"),
    # path('profile/<str:title>', profile , name = "profile"),
    #path('profile/<int:my_class>/<int:my_id>', profile , name = "profile"),
    path('profile/<str:my_class>/<int:my_id>/', profile , name = "profile"),
    #path('profile/<yyyy:year>', profile , name = "year"),
]
