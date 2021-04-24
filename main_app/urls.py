from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
]
