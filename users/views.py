from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import EmailRecipients

from neighbourhood.models import Profile
from users.email import send_welcome_email
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    '''
    Register a new user on registration and create user profile using signals
    '''
    if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        #username = form.cleaned_data.get('username')
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        #welcome email
        recipient = EmailRecipients(name = username,email =email)
        recipient.save()
        send_welcome_email(username,email)
        #succesful log in message
        messages.success(request, f'Your nyumba kumi account had been created successfully')
        
        return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
    
@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()

            messages.success(request, f'Your nyumba kumi account had been updated successfully')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
      'u_form':u_form,
      'p_form': p_form,
    }
    return render(request,'users/profile.html', context)
