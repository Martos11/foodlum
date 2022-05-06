from dataclasses import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#this below is for the contact page
from django.forms import ModelForm
from foodie.models import *
from shopcart.models import *
from user_profile.models import *



class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='username')#help_text is the same as placeholder
    first_name = forms.CharField(max_length=50, help_text='First Name')
    last_name = forms.CharField(max_length=50, help_text='Last Name')
    email = forms.CharField(max_length=50, help_text='Email')
    
    
    class Meta:
        model = User  # user is a model created by default
        fields = ['username','first_name','last_name','email','password1','password2']
        
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'subject', 'message']
        
STATE = [
    ('Abia','Abia'),
    ('Abuja','Abuja'),
    ('Edo','Edo'),
    ('Kano','Kano'),
    ('Lagos','Lagos'),
    ('Ogun','Ogun'),
    ('Ph','Ph'),
]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['first_name','last_name','phone','address','state','image']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address'}),
            'state': forms.Select(attrs={'class': 'form-select', 'placeholder':'State'}, choices=STATE),
            'image': forms.FileInput()
        }
        
        
class ShopCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'how_spicey']