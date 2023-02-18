from django.shortcuts import render
from app.forms import NearHundred, LoneSum, StringSplosion, CatDog

# Create your views here.
def root(request):
    return render(request, "root.html")


def nearhundred_view(request):
    if request.method == "POST":
        form = NearHundred(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            # result = abs(n - 100) <= 10 or abs(n - 200) <= 10
            if abs(n - 100) <= 10 or abs(n - 200) <= 10:
                result = True
            else:
                result = False
            return render(request, "nearhundred.html", {"form": form, "result": result})
    else:
        form = NearHundred()
        return render(request, "nearhundred.html", {"form": form})


def stringsplosion_view(request):
    if request.method == "POST":
        form = StringSplosion(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            result = ""
            for x in range(0, len(n) + 1):
                result += n[:x]
            return render(
                request, "stringsplosion.html", {"form": form, "result": result}
            )
    else:
        form = StringSplosion()
        return render(request, "stringsplosion.html", {"form": form})


def catdog_view(request):
    if request.method == "POST":
        form = CatDog(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            count_cat = 0
            count_dog = 0
            for i in range(len(n) - 2):
                if n[i : i + 3] == "dog":
                    count_dog += 1
                if n[i : i + 3] == "cat":
                    count_cat += 1
            result = count_cat == count_dog
            return render(
                request,
                "catdog.html",
                {"form": form, "result": result},
            )
    else:
        form = CatDog()
        return render(request, "catdog.html", {"form": form})


def lonesum_view(request):
    if request.method == "POST":
        form = LoneSum(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            c = form.cleaned_data["c"]
            if a == b == c:
                result = 0
            if b == c:
                result = a
            if a == c:
                result = b
            if a == b:
                result = c
            else:
                result = a + b + c
            return render(request, "lonesum.html", {"form": form, "result": result})
    else:
        form = LoneSum()
        return render(request, "lonesum.html", {"form": form})
