from django import forms


class SumDouble(forms.Form):
    n = forms.IntegerField(label="First Number:")
    m = forms.IntegerField(label="Second Number:")


class SleepIn(forms.Form):
    weekday = forms.BooleanField(
        required=False, label="Is it a Weekday? Check Box if Yes"
    )
    vacation = forms.BooleanField(
        required=False, label="Are you on vacation? Check Box if Yes"
    )


class Diff21(forms.Form):
    n = forms.IntegerField(label="Number:")
