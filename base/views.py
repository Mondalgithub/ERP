from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, LeaveRequest
from .forms import LeaveRequestForm
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm
from .forms import Update, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def loginPage(request):

    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    context={'form':form}
    return render(request, 'base/login_register.html', context)

def home(request):
    return render(request, 'base/home.html')

@login_required(login_url='login')
def profile(request, pk):
    
    profiles = CustomUser.objects.all()
    context = {'profiles': profiles}


    return render(request, 'base/profile.html', context)

def crud(request,pk):
    form = Update()
    if request.method == 'POST':
        form = Update(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request, 'base/crud.html',context)

def Delete(request, pk):
    form = CustomUser.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('home')
    context={'obj': form}
    return render(request, 'base/Delete.html', context)



def submit_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('requests')  # Redirect to the leave requests page after submission
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LeaveRequestForm()

    context = {'form': form}
    return render(request, 'base/submit_leave_request.html', context)


def leave_requests(request):
    requests = LeaveRequest.objects.all()
    context = {'requests': requests}
    return render(request, 'base/leave_requests.html', context)

def accept_leave_request(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    leave_request.is_accepted = True
    leave_request.save()
    messages.success(request, 'Leave request acceptted')
    return redirect('requests')