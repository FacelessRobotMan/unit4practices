from django.shortcuts import render
from app.forms import Left2, Combo, First_Half

# Create your views here.

list = ["left2", "combo", "first_half"]


def root_view(request):
    return render(request, "root.html", {"list": list})


def detailed_view(request, name):
    if name == "left2":
        if request.method == "POST":
            form = Left2(request.POST)
            if form.is_valid():
                n = form.cleaned_data["n"]
                result = n[2:] + n[:2]
                return render(
                    request,
                    "details.html",
                    {"result": result, "form": form, "name": name},
                )
        form = Left2()
        return render(request, "details.html", {"form": form, "name": name})
    elif name == "combo":
        if request.method == "POST":
            form = Combo(request.POST)
            if form.is_valid():
                n = form.cleaned_data["n"]
                m = form.cleaned_data["m"]
                if len(n) < len(m):
                    result = n + m + n
                else:
                    result = m + n + m
                return render(
                    request,
                    "details.html",
                    {"form": form, "result": result, "name": name},
                )
        form = Combo()
        return render(request, "details.html", {"form": form, "name": name})
    elif name == "first_half":
        if request.method == "POST":
            form = First_Half(request.POST)
            if form.is_valid():
                n = form.cleaned_data["n"]
                if len(n) % 2 == 0:
                    string = len(n) // 2
                    result = n[:string]
                else:
                    result = n
                return render(
                    request,
                    "details.html",
                    {"form": form, "result": result, "name": name},
                )
        form = First_Half()
        return render(request, "details.html", {"form": form, "name": name})
