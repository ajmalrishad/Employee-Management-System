# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import messages



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
       # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')  # Display error message
            return render(request, 'register.html')
        
        if User.objects.filter(username=username,email=email).exists():
            messages.error(request, 'Username or email already exists')  # Display error message
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        #redirect to login page
        messages.success(request, "Account Created Successfully!", extra_tags='login')
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page upon successful login
        else:
            messages.error(request, "Invalid username or password.", extra_tags='login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile_view(request):
    # Assuming a Profile model with a OneToOneField relationship to User
    user_profile = request.user  # Access the profile information via related model

    if request.method == 'POST':
        # Capture data from form inputs
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # Update User model
        request.user.username = username
        request.user.email = email
        request.user.save()

        # Update Profile model if exists
        user_profile.phone = phone
        user_profile.address = address
        user_profile.save()

        return redirect('profile')  # Redirect to profile page after saving

    return render(request, 'profile.html', {'user_profile': user_profile})


@login_required
def profile_edit(request):
    # Access the user profile information
    user_profile = request.user  # Assuming a OneToOneField from Profile to User

    if request.method == 'POST':
        # Capture form data
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update User model
        request.user.username = username
        request.user.email = email
        request.user.save()
        #save the user
        user_profile.save()

        # Display success message
        messages.success(request, 'Profile updated successfully!',  extra_tags='profile')
        
        return redirect('profile')  # Redirect to the profile page after saving

    # Pass the user and profile data to the template
    return render(request, 'profile_edit.html', {'user_profile': user_profile})