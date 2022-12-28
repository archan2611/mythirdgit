from django.urls import path
from app1.views import *
app_name= 'pinky'

urlpatterns= [
    path('string1/',string1, name='string1'),
    path('string2/',string2, name='string2'),

]
