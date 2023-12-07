from django import forms
from mysite.models import Contact,newsletter


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    masage=forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    class Meta:
        

        model = Contact
        fields = '__all__'   


class newsletterform(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'