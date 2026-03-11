from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [

path('admin/', admin.site.urls),

path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('events/', views.events, name='events'),
path('gallery/', views.gallery, name='gallery'),
path('reports/', views.reports, name='reports'),
path('news/', views.news, name='news'),
path('volunteers/', views.volunteers, name='volunteers'),
path('downloads/', views.downloads, name='downloads'),
path('contact/', views.contact, name='contact'),

]