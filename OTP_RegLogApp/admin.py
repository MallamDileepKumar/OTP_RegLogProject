from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    List_display = ['username','email','password','conf_password','mobile']
    List_filter = ['username']

admin.site.register(User,UserAdmin)
