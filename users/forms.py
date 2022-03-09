from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, )
    last_name = forms.CharField(max_length=100, )
    email = forms.EmailField(help_text='Enter valid email')
    password1 = forms.CharField(
        label='Enter Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # User.username = forms.CharField( max_length=100, required=False)
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        help_texts = {
            'username': None,
        }
        
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].required = False
            
            
            
class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, )
    last_name = forms.CharField(max_length=100, )
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email',]
        help_texts = {
            'username': None,
        }
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].required = False
            
 
class DateInput(forms.DateInput):
    input_type = 'date' 
            
class ExtendedProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False, label='Profile Picture' )
    birthdate = forms.DateField(widget=DateInput)
    class Meta:
        model = Profile
        fields = ['birthdate', 'gender', 'bio', 'photo']

