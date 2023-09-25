from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import UploadedFile
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("upload")
    else:
        form = UserCreationForm()
    return render(request, "registration/registration_form.html", {"form": form})


@login_required
def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        user = request.user
        uploaded_file_instance = UploadedFile(user=user, file=uploaded_file)
        uploaded_file_instance.save()
        # Handle file upload success
        return redirect('upload_success')
    return render(request, "registration/upload_form.html")

@login_required
def upload_success(request):
    return render(request, 'registration/upload_success.html')