from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite.models import Contact
from mysite.forms import NameForm,ContactForm,newsletterform
from django.contrib import messages
def index_view(reguest):
    return render(reguest,'website/index.html')

def about_view(reguest):
    return render(reguest,'website/about.html')

def contact_view(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        if form.is_valid():
            form.save()
            messages.add_message(reguest, messages.SUCCESS,'your tiket submitted successfuly')
        else:
            messages.add_message(reguest, messages.SUCCESS,'your tiket dident submitted ')
    form = ContactForm()        
    return render(reguest,'website/contact.html',{"form": form})


def newsletter_view(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    form = ContactForm()    
    #return render(reguest,'test.html',{"form": form})


def test_view(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("/thanks/")
        else:
            return HttpResponse("/not done/")
    form = ContactForm()    
    return render(reguest,'test.html',{"form": form})



