from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            form.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


"""
nothing can preventing me from going back to user profile
check place to make user login to access this page

-!-!-!- login_required is adding functionality to our profile view
user must be login to view this page

if not logged in
Request Method:	GET
Request URL:	http://127.0.0.1:8000/accounts/login/?next=/profile/
ERROR shows up
thus, we need to tell django where can find login route
by adding login_url into settings.py
"""


@login_required
def profile(request):
    return render(request, 'users/profile.html')
