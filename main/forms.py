from main.models import *
from django import forms
from django.core.validators import validate_email
from main.form_choices import *

class mainForm(forms.ModelForm):
    dpoa = forms.BooleanField(label = 'DPOA?')
    class Meta:
        model = checkupForm
        fields = [ 'first_name', 'last_name', 'email', 'age', 'dpoa']
        widgets = {
                'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
                'email': forms.TextInput(attrs={'placeholder': 'Email'}),
                'age': forms.TextInput(attrs={'placeholder': 'Age'}),



        }
    def __init__(self, *args, **kwargs):
        super(mainForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False

class SearchHillsPriors(forms.Form):

    prior_conviction = forms.ChoiceField(
                                        required = True,
                                        choices = YN_CHOICES
                                        )

    first_name = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'First Name',
                                })
                                )
    last_name = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'Last Name',
                                })
                                )
    dob = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'DOB: mm/dd/yr',
                                })
                                )
