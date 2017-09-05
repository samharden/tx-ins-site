from main.models import *
from django import forms
from django.core.validators import validate_email
from main.form_choices import *



class proof_of_loss(forms.Form):

    insurer = forms.ChoiceField(
                                        required = True,
                                        label='Insurer',
                                        choices = INSURER
                                        )

    policy_number = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'Policy Number',
                                })
                                )
    policy_term = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'Policy Term',
                                })
                                )
    bldg_cov = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'Amount of Ins. Coverage for Building',
                                })
                                )
    contents_cov = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'Amount of Ins. Coverage for Contents',
                                })
                                )
    insured_name = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'Name of Policyholder',
                                })
                                )
    loss_type = forms.ChoiceField(
                                        required = True,
                                        label='Type of Loss',
                                        choices = LOSS_TYPE
                                        )
    loss_time = forms.ChoiceField(
                                        required = True,
                                        label='Time of Loss',
                                        choices = TIME_CHOICES
                                        )
    loss_day = forms.ChoiceField(
                                        required = True,
                                        label='Day of Loss',
                                        choices = DAY_CHOICES
                                        )
    loss_month= forms.ChoiceField(
                                        required = True,
                                        label='Loss Month',
                                        choices = MONTH_CHOICES
                                        )
    loss_year = forms.ChoiceField(
                                        required = True,
                                        label='Loss Year',
                                        choices = YEAR_CHOICES
                                        )


    loss_cause = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'Cause of Loss',
                                })
                                )
    occupancy_type = forms.ChoiceField(
                                        required = True,
                                        label='Time of Loss',
                                        choices = YN_CHOICES
                                        )

    other_prop_interests = forms.ChoiceField(
                                        required = True,
                                        label='Time of Loss',
                                        choices = YN_CHOICES
                                        )
