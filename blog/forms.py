# -*- coding: utf-8 -*-

"""Functions for handling forms."""

__author__ = "M. Ziemba"
__date__ = "2012-09-05, 21:22"

import django.contrib.auth.forms as forms


class CustomRegistrationForm(forms.UserCreationForm):
    """Custom registration form, used for overriding default error
    messages.
    """

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        self.error_messages['duplicate_username'] = ("Podany login jest już zajęty")
        self.error_messages['password_mismatch'] = ("Podane hasła nie zgadzają się")

        self.fields['username'].error_messages = {
            'invalid': ("To pole może zawierać jedynie litery, cyfry lub znaki @/./+/-/_"),
            'required': ('Pole jest wymagane')}
        self.fields['password1'].error_messages = {'required': ('Pole jest wymagane')}
        self.fields['password2'].error_messages = {'required': ('Pole jest wymagane')}
