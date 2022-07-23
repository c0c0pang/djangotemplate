from django.urls import path
from . import views
app_name = "user"
urlpatterns = [
    path("main", views.main_view, name="login"),
    path("signup", views.signup_view, name="signup"),
    path("logout", views.logout_view, name="logout"),
]
