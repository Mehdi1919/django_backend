from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    address = forms.CharField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['address', 'agreement', 'city', 'cnic', 'comment', 'dob', 'gender', 'hobby', 'phone', 'postalCode','image']

    def clean(self):
        cleaned_data =  super().clean()
        
        fields_clean = ['address', 'agreement', 'city', 'cnic', 'comment', 'dob', 'gender', 'hobby', 'phone', 'postalCode']
        
        for field in fields_clean:
            value = cleaned_data.get(field)
            if value and str(value).startswith('-'):
                self.add_error(field,"Cannot start from negative!")
                
        return cleaned_data