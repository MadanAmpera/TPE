from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

'''from .models import students
from .models import progress
from .models import subject
from .models import teachers'''


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    # return HttpResponse("LOGIN PAGE!")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('admin')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})


def adminboard(request):
    return HttpResponse("ADMIN DASHBOARD!")


def studentreg(request):
    # return HttpResponse("Student Registration page!")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # the below set of lines not really needed,
            # Need to include other fields like parent names etc.

            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('admin')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})



