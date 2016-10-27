from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_user(request):
    if request.method == 'POST':
        # Create a user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        # Render an empty form
        form = UserCreationForm()
    return render(request,
        'accounts/register.html', {'user_create_form': form})
