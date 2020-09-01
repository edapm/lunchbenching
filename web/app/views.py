from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# Create your views here.

def home(request):
    context = {}
    return render(request, 'app/home.html', context)

def benches(request, pk):
    bench = Bench.objects.get(id=pk)

    form = CreateBenchForm()
    context={'form': form, 'bench': bench}
    return render(request, 'app/bench.html', context)

def benchlist(request):
    benches = Bench.objects.all()

    context = {'benches':benches}
    return render(request, 'app/benches.html', context)
