from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person

admin.site.register(Person)
# Register your models here.
