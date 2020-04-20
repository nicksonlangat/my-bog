from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeForm, PasswordChangeView
from .views import register, Profile, update


urlpatterns = [
    path('profile/', Profile.as_view(), name="profile"),
    path('profile/update/',  update, name="update"),
    path('signup/', register, name='signup'),
    path('login/', LoginView.as_view(template_name="account/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path('password/', PasswordChangeView.as_view(template_name='account/change_password.html'), name='change_password'),
]