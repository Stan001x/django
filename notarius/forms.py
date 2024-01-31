from django import forms
from django.db import models
from django.forms import SelectDateWidget

from .models import Report, PurposeOfAssessment, ClientPersonData


# class AddReport(forms.ModelForm):
#     conrtractDate = forms.DateField(
#             widget=SelectDateWidget(
#                 empty_label=("Choose Year", "Choose Month", "Choose Day"),
#             ), initial=Report.conrtractDate)
#     class Meta:
#         model = Report
#         fields = ['contractNumber', 'conrtractDate', 'image', ]

class UpdateReport(forms.ModelForm):
    conrtractDate = forms.DateField(
            widget=SelectDateWidget(
                empty_label=("Choose Year", "Choose Month", "Choose Day"),
            ), initial=Report.conrtractDate)
    class Meta:
        model = Report
        fields = ['contractNumber', 'conrtractDate', 'image', ]


class CreateReport(forms.ModelForm):

    class Meta:
        model = Report
        fields = "__all__"
        required = (
            'contractNumber',
        )


class CreatePurposeOfAssessment(forms.ModelForm):

    class Meta:
        model = PurposeOfAssessment
        fields = '__all__'



class CreatePersonDataForm(forms.ModelForm):

    class Meta:
        model = ClientPersonData
        fields = '__all__'
# class UpdateClientData(forms.ModelForm):
#     class Meta:
#         model = ClientData
#         fields = ['clientFullName', 'clientAdress', ]



#    contractNumber = forms.IntegerField()
#    conrtractDate = forms.DateField(
#        widget=SelectDateWidget(
#            empty_label=("Choose Year", "Choose Month", "Choose Day"),
#        ),)
#    clientname = forms.CharField()
#    image = forms.ImageField()