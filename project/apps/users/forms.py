from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


# ============================= USERCREATIONFORM ============================= #


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


# ============================== USERPROFILEFORM ============================= #

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "address",
            "telegram",
            "instagram",
        ]
