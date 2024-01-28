from django import forms
from django.db import models
from django.forms import SelectDateWidget

from .models import Report

class AddReport(forms.ModelForm):
    conrtractDate = forms.DateField(
            widget=SelectDateWidget(
                empty_label=("Choose Year", "Choose Month", "Choose Day"),
            ), initial=Report.conrtractDate)
    class Meta:
        model = Report
        fields = ['contractNumber', 'conrtractDate', 'clientname', 'image', ]

class UpdateReport(forms.ModelForm):
    conrtractDate = forms.DateField(
            widget=SelectDateWidget(
                empty_label=("Choose Year", "Choose Month", "Choose Day"),
            ), initial=Report.conrtractDate)
    class Meta:
        model = Report
        fields = ['contractNumber', 'conrtractDate', 'clientname', 'image', ]



#    contractNumber = forms.IntegerField()
#    conrtractDate = forms.DateField(
#        widget=SelectDateWidget(
#            empty_label=("Choose Year", "Choose Month", "Choose Day"),
#        ),)
#    clientname = forms.CharField()
#    image = forms.ImageField()