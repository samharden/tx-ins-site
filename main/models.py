from django.db import models

# Create your models here.
import pandas as pd
from pandas import DataFrame
import sqlalchemy as sa
from django.db.models.aggregates import Count
from random import randint


class checkupForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dpoa = models.BooleanField()
    year_dpoa = models.CharField(max_length=100)
    hc_proxy = models.CharField(max_length=100)
    year_hc_proxy = models.CharField(max_length=100)
    will = models.CharField(max_length=100)
    year_will = models.CharField(max_length=100)
    trust = models.CharField(max_length=100)
    year_trust = models.CharField(max_length=100)
