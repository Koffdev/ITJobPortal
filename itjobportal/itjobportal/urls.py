from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from job.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='job/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('job/<slug:slug>', job, name="job"),
    path('apply-job/<int:id>/', apply_job, name='apply-job'),
    path('requests/', user_requests, name='requests'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit-profile')
]
