"""
URL configuration for tobify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth_app.views import (
    notes_view, new_note_view, edit_note, delete_note, register_page, 
    login_page, verify_email, resend_mail, new_note, about, note_detail, 
    log_out, home, toggle_note_visibility
)
from get_attendence import views as vw
urlpatterns = [
    path('admin-tobi-tech/', admin.site.urls),
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('verify/', verify_email, name='verify_email'),
    path('resend/', resend_mail, name='resend_mail'),
    path('new/', new_note, name='new_note'),
    path('about/', about, name='about'),
    path('attendence/', vw.get_attendence, name='get_attendence'),
    path('logout/', log_out, name='logout'),
    path('notes/', notes_view, name='notes'),
    path('toggle-note-visibility/<str:note_id>/', toggle_note_visibility, name='toggle_note_visibility'),
    path('notes/new/', new_note_view, name='new_note'),
    path('notes/<str:note_id>/edit/', edit_note, name='edit_note'),
    path('notes/<str:note_id>/delete/', delete_note, name='delete_note'),
    path('notes/<str:note_id>/', note_detail, name='note_detail'),
    path('', home, name='home')
]
