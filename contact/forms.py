from django import forms

from .models import ContactMessage

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'contact_input', 'placeholder': 'Your name'}),max_length=64, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class' : 'contact_input', 'placeholder': 'Your email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'contact_input', 'placeholder': 'Subject'}),max_length=128, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'contact_input_comments contact_input_comments inpt', 'placeholder': 'Message'}), required=True)
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'subject', 'message')
#
# class UserSignInForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.EmailInput(attrs={'class' : 'contact_input', 'placeholder': 'Your email'}),max_length=100, required=True)
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'contact_input', 'placeholder': 'Your password'}))
#     # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'contact_input', 'placeholder': 'Confirm your password'}))
#     class Meta:
#         model = User
#         fields = ('username', 'password1')
