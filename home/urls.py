
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Login to Burhan"
admin.site.site_title = "Welocom to DashBord"
admin.site.index_title = "Welocom to Portal"



urlpatterns = [
    path('', views.home, name='home'),
    path('project', views.project, name='project'),
    path('project1', views.project1, name='project1'),
    path('project2', views.project2, name='project2'),
    path('project3', views.project3, name='project3'),
]
