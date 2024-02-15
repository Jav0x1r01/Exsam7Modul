from django.contrib import admin

from apps.models import UserListModel


# Register your models here.
@admin.register(UserListModel)
class UserAdmin(admin.ModelAdmin):
    pass