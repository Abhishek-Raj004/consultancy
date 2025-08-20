# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('services',views.service, name='services'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('team',views.team, name='team'),
    path('portfolio',views.portfolio, name='portfolio'),

]