from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

#newly added function
def update_profile_adding_mobile(user):
    Profile.objects.update_or_create(user=user, defaults={'mobile': user.profile.mobile})

def register(request):
    if request.method == 'POST':  # there are two main methodes get and post (post for sending information) here check what methode
        form = UserRegisterForm(request.POST)  # request.post is for getting the content of registration
        if form.is_valid():  # check if the form is valid
            user = form.save()  # for saving user
            user.profile.mobile = form.cleaned_data.get('mobile')
            update_profile_adding_mobile(user)
            username = form.cleaned_data.get('username')  # get the unsername of the user
            messages.success(request, f'Account created for {username}!')  # for showing success message after creation
            return redirect(
                'blog-home')  # After the successfully creation we have to redirect to other page 'blog-home' is name
    else:
        form = UserRegisterForm()  # if the form isn't post then we gonna send an empty form because it's get
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, #for files in our case images
                                   instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')  # get the unsername of the user
            messages.success(request, f'user and profile updated for {username}!')
            return redirect("profile") # redirecting here cause a get method so it's prevent us of getting repost when rendering
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, "users/profile.html", context)
