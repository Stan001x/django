from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notarius:index')
    form = NewUserForm()
    context={
        'form':form
    }
    return render(request, 'users/register.html', context)

@login_required

def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("contact_number")
        image = request.FILES['upload']
        user = request.user
        item = Profile(user=user, contact_number=contact_number, image=image)
        item.save()
    return render(request, 'users/profile.html')
