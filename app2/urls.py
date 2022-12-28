from django.urls import path
from app2.views import *
app_name = 'pinky1'

urlpatterns = [
    path('htmlfile1/',htmlfile1,name='htmlfile1'),
    path('htmlfile2/',htmlfile2,name='htmlfile2'),
]