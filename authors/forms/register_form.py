
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from recipes.models import Recipe
from utils.django_forms import add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username here')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['password2'], 'Repeate your password')

    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        required=True,
        label='First name',
    )

    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        required=True,
        label='Last name',
    )

    username = forms.CharField(
        label='Username',
        help_text=(
            'Username must have letters, numbers or one of those @ . + - _ . '
            'Then length should be between 4 and 15 characters.'
        ),
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 charecters',
            'max_length': 'Username must have at less than 150 charecters',
        },

        min_length=4, max_length=150,

    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must be have at least one uppercase letter,'
            'one lowercase letter and one numerber. '
            'The length should be at least 8 characters'
        ),
        validators=[strong_password],
        label='Password',
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Password2',
        error_messages={
            'required': 'Please, repeat your password'
        },
    )

    email = forms.EmailField(
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text=(
            'The e-mail must be valid'
        ),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        widgets = {

            'password': forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is arealdy in use', code='invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Password and Password2 must be equal',
                'password2': 'Password and Password2 must be equal',
            })
