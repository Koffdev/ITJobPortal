from django.contrib import admin
from .models import Job, Category, UserRequest, Profile


admin.site.register(Category)
admin.site.register(Job)
admin.site.register(UserRequest)
admin.site.register(Profile)
