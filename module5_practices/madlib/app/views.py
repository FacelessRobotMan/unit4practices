from django.shortcuts import render
from app.forms import MadLibForm

# Create your views here.
def MadLibView(request):
    if request.method == "POST":
        form = MadLibForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            name = form.cleaned_data["name"]
            adjective = form.cleaned_data["adjective"]
            noun = form.cleaned_data["noun"]
            signed = form.cleaned_data["signed"]

            context = {
                "form": form,
                "date": date,
                "name": name,
                "adjective": adjective,
                "noun": noun,
                "signed": signed,
            }
            return render(request, "madlib.html", context)

    else:
        form = MadLibForm()
        return render(request, "madlib.html", {"form": form})
