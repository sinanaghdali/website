from django.urls import path
from mysite.views import *

app_name='mysite'

urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view,name='about'), 
    path('contact',contact_view,name='contact'),
    path('newsletter',newsletter_view,name='newsletter'),
    path('test',test_view,name='test'),
] 


