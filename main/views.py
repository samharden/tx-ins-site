from django.shortcuts import render
from main.forms import *
import pandas as pd
# Create your views here.
def home_page(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def criminal_defense(request):
    return render(request, 'main/criminal-defense.html')

def wte_page(request):

    return render(request, 'main/wills-trusts-estates.html')

def seal_crim(request):

    form = SearchHillsPriors()
    name = ""
    df = ''

    # def my_custom_sql(self):
    engine = sa.create_engine('mysql://root:sq8337269!@104.196.179.105:3306/voyansqldb?')
    if request.method == 'POST':
        print("POST")
        form = SearchHillsPriors(request.POST)
        # print(request.POST['name'])
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            dob = form.cleaned_data['dob']
            full_name = last_name+', '+first_name
            print(full_name)

            sql_text = """SELECT DISTINCT CASENO,
                                CNT,
                                CHARGEDESCRIPTION,
                                DISPO
                                FROM stn_searchhillspriorsall
                                WHERE DEFENDANTNAME
                                REGEXP '%s'
                                AND DOB = '%s'
                                ;""" % (full_name, dob)
            df = pd.read_sql_query(sql_text, engine)


            case_dispo = df['DISPO']
            df = df.replace('NT - LETTER OF RELEASE', 'Potentially')
            df = df.replace('NT - DISMISSED', 'Potentially')
            df = df.replace('NT - ADJUDICATION WITHHELD', 'Potentially')
            df.columns = ['Case No:','Count:','Charge:','Can Seal/Expunge:']


            case_amt = len(case_dispo)

            empty_dict = {          'Can Seal/Expunge:':[],
                                    'Case No:':[],
                                    'Count:':[],
                                    'Charge:':[],
                                    }
            for x in range(0, case_amt):
                casenum = df.iloc[x]['Case No:']
                empty_dict['Case No:'].append(casenum)
                count = df.iloc[x]['Count:']
                empty_dict['Count:'].append(count)
                charge = df.iloc[x]['Charge:']
                empty_dict['Charge:'].append(charge)
                sealability = df.iloc[x]['Can Seal/Expunge:']
                empty_dict['Can Seal/Expunge:'].append(sealability)

            return render(request, 'main/sealing-criminal-record.html',
                                    {'form':form,
                                    'df':df.to_html,
                                    'case_amt': case_amt,
                                    'empty_dict':empty_dict,
                                    })
        else:
            form = SearchHillsPriors()

    return render(request, 'main/sealing-criminal-record.html', {'form':form})

def injunctions(request):
    return render(request, 'main/injunctions.html')

def checkup(request):
    form = mainForm()
    return render(request, 'main/legal-checkup.html', {'form':form})
