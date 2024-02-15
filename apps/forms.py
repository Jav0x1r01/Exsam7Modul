from django import forms
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

from apps.models import UserListModel




class UserForm(forms.ModelForm):
    class Meta:
        model = UserListModel
        fields = ('rasm', 'username', 'first_name', 'last_name', 'description', 'email', 'website')
        # exclude = ('created_at',)
