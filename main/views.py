from django.shortcuts import render
from main.forms import *
import pandas as pd
# Create your views here.
def home_page(request):
    return render(request, 'main/home.html')
