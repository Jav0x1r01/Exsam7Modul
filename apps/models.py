from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, DecimalField, FloatField, ImageField, EmailField,URLField
from django_ckeditor_5.fields import CKEditor5Field


class UserListModel(Model):
    rasm = ImageField(upload_to='media/user/')
    username = CharField(max_length=255)
    first_name=CharField(max_length=255)
    last_name=CharField(max_length=255)
    email=EmailField(max_length=255)
    website=URLField(max_length=255)
    description = CKEditor5Field(blank=True, null=True, config_name='extends')

