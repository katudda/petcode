from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password1 = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        required=True,
        label='Password confirmation',
        widget=forms.PasswordInput
    )
    first_name = forms.CharField(
        required=False,
        label = 'First Name',
        max_length = 30,
    )
    last_name = forms.CharField(
        required=False,
        label = 'Last Name',
        max_length = 30,
    )