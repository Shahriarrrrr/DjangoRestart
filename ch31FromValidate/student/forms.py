from django import forms

# class Registration(forms.Form):
#     name  = forms.CharField()
#     email  = forms.EmailField()
#     password = forms.CharField(widget= forms.PasswordInput)


#     """Below the function name cant be random 
#     It should be clean_field that i want to validate or clean"""
#     def clean_name(self):
#         #name  = self.cleaned_data('name')
#         name_val = self.cleaned_data['name']
#         print(name_val)
#         if len(name_val) < 5 :
#             raise forms.ValidationError("Enter more than or equal 5 char ")
#         return name_val
    

#Clean all fields at once:

class Registration(forms.Form):
    name  = forms.CharField()
    email  = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput)



    def clean(self):
        cleaned_data = super().clean()
        name_value  = cleaned_data.get('name')
        email_value  = cleaned_data.get('email')
        if name_value and len(name_value) < 4:
            self.add_error('name', 'Enter more char')
    
        if email_value and len(email_value) < 15:
            self.add_error('email', 'Enter more char')
    
