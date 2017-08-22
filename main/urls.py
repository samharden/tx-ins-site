from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^about', views.about, name='about'),
    url(r'^criminal-defense', views.criminal_defense, name='criminal-defense'),
    url(r'^injunctions', views.injunctions, name='injunctions'),
    url(r'^sealing-criminal-record', views.seal_crim, name='sealing-criminal-record'),
    url(r'^wills-trusts-estates', views.wte_page, name='wills-trusts-estates'),
    url(r'^legal-checkup', views.checkup, name='legal-checkup'),

]
