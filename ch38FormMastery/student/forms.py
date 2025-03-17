from django import forms
from .models import Profile

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

JOB_CITY_CHOICE = [
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Barishal', 'Barishal'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
    ('Comilla', 'Comilla'),
    ('Narayanganj', 'Narayanganj'),
]


class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices= GENDER_CHOICES,
        widget = forms.RadioSelect
    )
    job_city = forms.MultipleChoiceField(
        choices=JOB_CITY_CHOICE,
        widget=forms.CheckboxSelectMultiple,
        label= "Preffered Job Cities",
        help_text="Choose cities you can work in"
    )
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'name' : 'Full Name',
            'dob' : 'Date of Birth',
            'pin' : 'Pin Code',
            'mobile': 'Mobile Number',
            'job_city': 'Job City'
        }
        help_texts = {
            'profile_image': 'Optional : Upload a profile image',
            'my_file': 'Optional: Attatch any additional document(PDF, DOCX, etc)',
            #Bellow it wont work because declared before 
            #'job_city': 'Enter Citites you can work in or have worked'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.TextInput(attrs={'class': 'form-control', 'id': 'datepicker', 'type' : 'date'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Write your area name'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }
