from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':  # there are two main methodes get and post (post for sending information) here check what methode
        form = UserRegisterForm(request.POST)  # request.post is for getting the content of registration
        if form.is_valid():  # check if the form is valid
            form.save()  # for saving user
            username = form.cleaned_data.get('username')  # get the unsername of the user
            messages.success(request, f'Account created for {username}!')  # for showing success message after creation
            return redirect(
                'blog-home')  # After the successfully creation we have to redirect to other page 'blog-home' is name
    else:
        form = UserRegisterForm()  # if the form isn't post then we gonna send an empty form because it's get
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, "users/profile.html")
