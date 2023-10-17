from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View

# ============================================================================ #
from project.apps.users.forms import UserCreationForm


class Register(View):
    template_name = "registration/register.html"

    def get(self, request):
        form = UserCreationForm()

        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")

        context = {"form": form}

        return render(request, self.template_name, context)
