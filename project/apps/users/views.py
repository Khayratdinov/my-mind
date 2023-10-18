from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ============================================================================ #
from project.apps.users.forms import UserCreationForm, UserProfileForm


# ================================= REGISTER ================================= #


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


# ================================ USERPROFILE =============================== #


@method_decorator(login_required, name="dispatch")
class UserProfile(View):
    template_name = "registration/profile.html"

    def get(self, request):
        user = request.user
        context = {"user": user}
        return render(request, self.template_name, context)


# ================================ EDITPROFILE =============================== #


@method_decorator(login_required, name="dispatch")
class EditProfile(View):
    template_name = "registration/edit_profile.html"

    def get(self, request):
        form = UserProfileForm(instance=request.user)
        context = {"form": form}
        print("FORM", form)
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("index")

        context = {"form": form}
        return render(request, self.template_name, context)
