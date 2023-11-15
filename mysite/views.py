from django.shortcuts import render


from django.http import HttpResponse

def index_view(reguest):
    return HttpResponse('<h1> home page </h1>')

def about_view(reguest):
    return HttpResponse('<h1> about page </h1>')

def contact_view(reguest):
    return HttpResponse('<h1> contct page </h1>')
