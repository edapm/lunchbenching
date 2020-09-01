from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import *
from . forms import *

# Create your views here.

def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'app/login.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context={'form':form}
    return render(request, 'app/register.html', context)

def home(request):
    context = {}
    return render(request, 'app/home.html', context)

def benches(request, pk):
    bench = Bench.objects.get(id=pk)

    context={'bench': bench}
    return render(request, 'app/bench.html', context)

def benchlist(request):
    all_benches = Bench.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_benches, 4)

    try:
        benches = paginator.page(page)
    except PageNotAnInteger:
        benches = paginator.page(1)
    except EmptyPage:
        benches = paginator.page(paginator.num_pages)

    context = {'benches':benches}
    return render(request, 'app/benches.html', context)

def CreateBench(request):
    form = CreateBenchForm()

    context = {'form':form}
    if request.method == 'POST':
        form = CreateBenchForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            return redirect('/b')

    return render(request, 'app/create.html', context)

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
            return redirect('/b')

    return render(request, 'app/update.html', context)

def DeleteBench(request, pk):
    bench = Bench.objects.get(id=pk)
    if request.method == "POST":
        bench.delete()
        return redirect('bench-list')
    
    name = bench.name

    context = {'item': bench, 'name': name}
    return render(request, 'app/delete.html', context)