from django.urls import path

from .views import *

app_name = 'base'

urlpatterns = [

    path('', l, name = 'l'),

    path('contact-us/', c, name = 'c'),
    path('c/', cs, name = 'cs'), # submit contact form

    path('terms/', t, name = 't'),
    path('privacy/', p, name = 'p'),
    path('juridical-information/', j, name = 'j'),
    
    #path('online-payment-safety/', ops, name = 'ops'),
    #path('data-safety/', ds, name = 'ds'),

]