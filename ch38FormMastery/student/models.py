from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError('The Pin code must be exactly 6 digits')

STATE_CHOICE = (
    ('Barisal', 'Barisal'),
    ('Chattogram', 'Chattogram'),
    ('Dhaka', 'Dhaka'),
    ('Khulna', 'Khulna'),
    ('Mymensingh', 'Mymensingh'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Sylhet', 'Sylhet'),
)



# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField(
        validators=[validate_pin_length],
        help_text='Enter 6 digit code')
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    mobile = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\d{11}$')],
        help_text= 'Enter only 11 digits')
    email = models.EmailField(max_length=100)
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to= 'doc', blank= True)
