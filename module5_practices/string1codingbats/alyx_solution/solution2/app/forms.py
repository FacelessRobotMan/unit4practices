from django import forms


class Left2(forms.Form):
    n = forms.CharField(label="Type a Word:", max_length=100, required=True)


class Combo(forms.Form):
    n = forms.CharField(label="Type a Word:", max_length=100, required=True)
    m = forms.CharField(label="Type a Word:", max_length=100, required=True)


class First_Half(forms.Form):
    n = forms.CharField(label="Type a Word:", max_length=100, required=True)
