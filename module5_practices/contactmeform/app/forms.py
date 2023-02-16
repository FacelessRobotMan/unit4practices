from django import forms


class ContactMeForm(forms.Form):
    first = forms.CharField(max_length=200)
    last = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(max_length=300)
