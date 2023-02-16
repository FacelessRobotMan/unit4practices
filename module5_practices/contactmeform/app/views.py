from django.shortcuts import render
from app.forms import ContactMeForm

# Create your views here.
def RootView(request):
    return render(request, "root.html")


def ContactMeView(request):
    if request.method == "POST":
        form = ContactMeForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data["first"]
            last = form.cleaned_data["last"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            context = {
                "form": form,
                "first": first,
                "last": last,
                "email": email,
                "message": message,
            }

            return render(request, "contactme.html", context)
    else:
        form = ContactMeForm()
        return render(request, "contactme.html", {"form": form})
