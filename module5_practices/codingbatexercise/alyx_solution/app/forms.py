from django import forms


class NearHundred(forms.Form):
    n = forms.IntegerField(label="Number Please, Sir:")


class StringSplosion(forms.Form):
    n = forms.CharField(label="String Please, Sir:", max_length=200)


class CatDog(forms.Form):
    n = forms.CharField(label="String Please, Sir:", max_length=200)


class LoneSum(forms.Form):
    a = forms.IntegerField(label="Number Please, Sir:")
    b = forms.IntegerField(label="Number Please, Sir:")
    c = forms.IntegerField(label="Number Please, Sir:")
