from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import RegistratonForm, UpdateProfile
from blog.models import Post



def register(request):
    if request.method == "POST":
        form = RegistratonForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"you've successfully registered as {username}")
            login(request, new_user)
            return redirect('/')
    else:
        form =RegistratonForm()
    return render(request,  'account/signup.html', {'form':form})




class Profile(LoginRequiredMixin, ListView):
    template_name = 'account/profile.html'
    paginate_by     =   3

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_on')


def update(request):
    if request.method == "POST":
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f"You've successfully updated your profile")
            return redirect("profile")
    else:
        form = UpdateProfile(instance=request.user)
    return render(request, 'account/update.html', {'form':form})





