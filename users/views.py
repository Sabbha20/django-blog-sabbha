
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm, ExtendedProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.


def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Registration successful for {username}')
            return redirect('blog:homepage')
    else:
        form = UserRegistrationForm()
    return render(req, 'users/register.html', {'form': form})

@login_required
def profile(req):
    return render(req, 'users/profile.html')

@login_required
def profileUpdate(req):
    if req.method == 'POST':
        user_form = UserProfileForm(req.POST, instance=req.user)
        
        extended_profile_form = ExtendedProfileForm(
            req.POST, req.FILES, instance=req.user.profile)
        
        
        if user_form.is_valid() and extended_profile_form.is_valid():
            user_form.save()
            extended_profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(
                req, f'Profile updated successfully for {username}')
            return redirect('profile')
    else:
        user_form = UserProfileForm(instance=req.user)
        extended_profile_form = ExtendedProfileForm(instance=req.user.profile)
        
        
    return render(req, 'users/profile_update.html', {'user_form': user_form,
                                                     'extended_profile_form': extended_profile_form})
    
    

class UserPasswordChangeView(PasswordChangeView):
    model = User
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('profile')




    
