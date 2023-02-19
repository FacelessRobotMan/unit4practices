from django import forms


class SumDouble(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()


class Diff21(forms.Form):
    a = forms.IntegerField()


class SleepIn(forms.Form):
    weekday = forms.BooleanField(required=False)
    vacation = forms.BooleanField(required=False)
