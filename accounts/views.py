from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login

# Create your views here.


def signup(request):
    # return render(request, "signup.html")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # checks if user is loged in
            user = form.save()
            # saves user instance to log them in right now
            login(request, user)
            # because prompt wants us to create user and log them in
            # login needs to take request, and user which contains username/pass
            return redirect("home")
    else:
        form = UserCreationForm()
        # this is neccessary because this form still needs to pass to load the page

    return render(request, "registration/signup.html", {"form": form})
    # form is the usercreation form
