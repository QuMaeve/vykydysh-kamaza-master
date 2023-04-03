from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name","last_name","patronymic",
            "email",
            "locality","classes","establishment","deleted",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name","last_name","patronymic",
            "email",
            "locality","classes","establishment","deleted",)