from django.shortcuts import render
from main.forms import *
import pandas as pd
# Create your views here.
def home_page(request):
    return render(request, 'main/home.html')

def claim_form(request):
    form = claim_form()
    if request.method == 'POST':
        form = claim_form(request.POST)
        if form.is_valid():
            print("Valid")
    else:
        form = claim_form()

        return render(request, 'main/claim-form.html', {'form':form})
