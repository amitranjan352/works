from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Snippet,Register,Login
admin.site.register(Snippet) 
admin.site.register(Register)
admin.site.register(Login)
