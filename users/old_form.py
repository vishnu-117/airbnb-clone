from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is wrong"))
        except User.DoesNotExist:
            raise forms.ValidationError("User Does not exist")


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("User already exists")
        except User.DoesNotExist:
            return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password = self.cleaned_data.get("password")

        if password1 != password:
            raise forms.ValidationError(
                "Password does not math. please enter again")
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "password1")
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password")

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password = self.cleaned_data.get("password")

        if password1 != password:
            raise forms.ValidationError(
                "Password does not math. please enter again")
        else:
            return password
