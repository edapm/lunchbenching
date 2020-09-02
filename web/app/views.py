from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from . models import *
from . forms import *
from . decorators import *

# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context = {'form': form}

    return render(request, 'app/login.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='normal-user')
            user.groups.add(group)
            Profile.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context={'form':form}
    return render(request, 'app/register.html', context)

@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):
    all_benches = Bench.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_benches, 4)

    try:
        benches = paginator.page(page)
    except PageNotAnInteger:
        benches = paginator.page(1)
    except EmptyPage:
        benches = paginator.page(paginator.num_pages)

    context = {'benches': benches}
    return render(request, 'app/home.html', context)

def benches(request, pk):
    bench = Bench.objects.get(id=pk)

    context={'bench': bench}
    return render(request, 'app/bench.html', context)

def userProfile(request, slug):
    slug = Profile.objects.get(slug=slug)

    context={'user':slug}

    return render(request, 'app/user.html', context)

def updateProfile(request):
    user = Profile.objects.get(user=request.user)
    form = UpdateProfileForm(instance=user)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
                form.save()
                return redirect('user', request.user)
    
    context = {'form': form}
    
    return render(request, 'app/user-edit.html', context)

def benchlist(request):
    return redirect('home')

@login_required(login_url='login')
def CreateBench(request):
    form = CreateBenchForm()

    context = {'form':form}
    if request.method == 'POST':
        form = CreateBenchForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            return redirect('home')

    return render(request, 'app/create.html', context)

@login_required(login_url='login')
def UpdateBench(request, pk):
    bench = Bench.objects.get(id=pk)
    form = CreateBenchForm(instance=bench)

    context = {'form': form}
    if request.method == 'POST':
        form = CreateBenchForm(request.POST, instance=bench)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            return redirect('home')

    return render(request, 'app/update.html', context)


@login_required(login_url='login')
def DeleteBench(request, pk):
    bench = Bench.objects.get(id=pk)
    if request.method == "POST":
        bench.delete()
        return redirect('bench-list')
    
    name = bench.name

    context = {'item': bench, 'name': name}
    return render(request, 'app/delete.html', context)
