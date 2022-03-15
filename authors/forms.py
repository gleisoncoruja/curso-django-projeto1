from attr import attr
from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'password': 'Password',
        }

        help_text = {
            'email': 'The e-mail must be valid',
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Type your username here'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here',
            })
        }
