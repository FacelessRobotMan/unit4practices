from django.shortcuts import render
from app.forms import SumDouble, Diff21, SleepIn

# Create your views here.
def root_view(request):
    return render(request, "root.html")


def sum_double(a, b):
    total = a + b
    if a == b:
        total = total * 2
    return total


def diff21(a):
    if a > 21:
        total = a - 21
    else:
        total = 21 - a
    return total


def sleepin(weekday, vacation):
    if vacation == True:
        return True
    if weekday == False:
        return True
    return False


def sleepin_view(request):
    if request.method == "POST":
        form = SleepIn(request.POST)
        if form.is_valid():
            weekday = form.cleaned_data["weekday"]
            vacation = form.cleaned_data["vacation"]
            context = {"form": form, "result": sleepin(weekday, vacation)}
            return context
    else:
        form = SleepIn()
        return {"form": form}


def diff21_view(request):
    if request.method == "POST":
        form = Diff21(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            context = {"form": form, "result": diff21(a)}
            return context
    else:
        form = Diff21()
        return {"form": form}


def sum_double_view(request):
    if request.method == "POST":
        form = SumDouble(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            context = {"form": form, "result": sum_double(a, b)}
            return context
    else:
        form = form = SumDouble()
        return {"form": form}


def detailed_view(request, path_name):
    if path_name == "sleepin":
        context = sleepin_view(request)
    elif path_name == "diff21":
        context = diff21_view(request)
    elif path_name == "sumdouble":
        context = sum_double_view(request)
    context["path_name"] = path_name
    return render(request, "details.html", context)
