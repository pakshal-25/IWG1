from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.forms import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post
from .models import Image
class SignUpForm(UserCreationForm):
    #password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #password2=forms.CharField(label='Confirm Your Password',widget=forms.PasswordInput({'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        #labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}
        #widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        #'first_name':forms.TextInput(attrs={'class':'form-control'}),
        #'last_name':forms.TextInput(attrs={'class':'form-control'}),
        #'email':forms.EmailInput(attrs={'class':'form-control'}),
        #}
#class LoginForm(AuthenticationForm):
    #username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    #password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current password','class':'form-control'}))
    

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        labels={'photo':''}

        
        