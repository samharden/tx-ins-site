from django.shortcuts import render
from main.forms import *
import pandas as pd
# Create your views here.
def home_page(request):
    return render(request, 'main/home.html')

def claim_form(request):
    form = proof_of_loss()
    if request.method == 'POST':
        form = proof_of_loss(request.POST)
        if form.is_valid():
            print("Valid")
            return render(request, 'main/claim-form.html', {'form':form})
    else:
        form = proof_of_loss()


    return render(request, 'main/claim-form.html', {'form':form})
