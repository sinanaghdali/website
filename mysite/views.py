from django.shortcuts import render


from django.http import HttpResponse

def index_view(reguest):
    return render(reguest,'website/index.html')

def about_view(reguest):
    return render(reguest,'website/about.html')

def contact_view(reguest):
    return render(reguest,'website/contact.html')
 