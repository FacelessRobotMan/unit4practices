from django.shortcuts import render
from app.forms import SumDouble, Diff21, SleepIn

# Create your views here.


def root_view(request):
    return render(request, "root.html")


def sum_double(request):
    if request.method == "POST":
        form = SumDouble(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            m = form.cleaned_data["m"]
            result = n + m
            if n == m:
                result = result * 2
            return render(request, "sum.html", {"result": result, "form": form})
    form = SumDouble()
    return render(request, "sum.html", {"form": form})


def diff21(request):
    if request.method == "POST":
        form = Diff21(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            if n <= 21:
                result = 21 - n
            else:
                result = (n - 21) * 2
            return render(request, "diff21.html", {"form": form, "result": result})
    form = Diff21()
    return render(request, "diff21.html", {"form": form})


def sleep_in(request):
    if request.method == "POST":
        form = SleepIn(request.POST)
        if form.is_valid():
            weekday = form.cleaned_data["weekday"]
            vacation = form.cleaned_data["vacation"]
            result = False
            if weekday == False:
                result = True
            if vacation == True:
                result = True
            return render(request, "sleepin.html", {"form": form, "result": result})
    form = SleepIn()
    return render(request, "sleepin.html", {"form": form})
