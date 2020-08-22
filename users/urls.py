from django.urls import path
from .views import LoginView, log_out, SignupView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", log_out, name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
]
