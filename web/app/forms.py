from django import forms
from django.forms import ModelForm
from . models import *

class CreateBenchForm(ModelForm):
    class Meta:
        model = Bench
        fields = '__all__'
