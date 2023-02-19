from django.shortcuts import render
from app.forms import Left2, Combo, First_Half

# Create your views here.


def root_view(request):
    return render(request, "root.html")


def left2(request):
    if request.method == "POST":
        form = Left2(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            result = n[2:] + n[:2]
            return render(request, "left2.html", {"result": result, "form": form})
    form = Left2()
    return render(request, "left2.html", {"form": form})


def combo(request):
    if request.method == "POST":
        form = Combo(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            m = form.cleaned_data["m"]
            if len(n) < len(m):
                result = n + m + n
            else:
                result = m + n + m
            return render(request, "combo.html", {"form": form, "result": result})
    form = Combo()
    return render(request, "combo.html", {"form": form})


def first_half(request):
    if request.method == "POST":
        form = First_Half(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            if len(n) % 2 == 0:
                string = len(n) // 2
                result = n[:string]
            else:
                result = n
            return render(request, "firsthalf.html", {"form": form, "result": result})
    form = First_Half()
    return render(request, "firsthalf.html", {"form": form})
