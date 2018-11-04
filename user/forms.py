from django import forms

from django.contrib.auth.models import User

# class UserSignUpForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.EmailInput(attrs={'class' : 'contact_input', 'placeholder': 'Your email'}),max_length=100, required=True)
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'contact_input', 'placeholder': 'Your password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'contact_input', 'placeholder': 'Confirm your password'}))
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
#
# class UserSignInForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.EmailInput(attrs={'class' : 'contact_input', 'placeholder': 'Your email'}),max_length=100, required=True)
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'contact_input', 'placeholder': 'Your password'}))
#     # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'contact_input', 'placeholder': 'Confirm your password'}))
#     class Meta:
#         model = User
#         fields = ('username', 'password1')
