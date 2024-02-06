from django import forms
from django.db import models
from django.forms import SelectDateWidget

from .models import Report, PurposeOfAssessment, ClientPersonData, ObjectOfAssessment


# class AddReport(forms.ModelForm):
#     conrtractDate = forms.DateField(
#             widget=SelectDateWidget(
#                 empty_label=("Choose Year", "Choose Month", "Choose Day"),
#             ), initial=Report.conrtractDate)
#     class Meta:
#         model = Report
#         fields = ['contractNumber', 'conrtractDate', 'image', ]

class UpdateReport(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['contractNumber', 'conrtractDate', 'image', ]



class CreateReport(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['contractNumber', 'conrtractDate', 'reportNumber', 'dateOfAssessment', 'dateOfReport', 'documentsOfReport', 'purposeOfAssessment', 'clientName']
        required = (
            'contractNumber',
        )
        widgets = {
            'conrtractDate': forms.TextInput(attrs={'type': 'date'}),
#            'clientName': forms.TextInput(attrs={'class': '1'}),
            'dateOfAssessment': forms.TextInput(attrs={'type': 'date'}),
            'dateOfReport': forms.TextInput(attrs={'type': 'date'}),
        }


class CreatePurposeOfAssessment(forms.ModelForm):

    class Meta:
        model = PurposeOfAssessment
        fields = '__all__'



class CreatePersonDataForm(forms.ModelForm):

    class Meta:
        model = ClientPersonData
        fields = '__all__'

        widgets = {
            'clientPasportDate': forms.TextInput(attrs={'type': 'date'}),
            }


class ObjectOfAssessmentForm(forms.ModelForm):
    class Meta:
        model = ObjectOfAssessment
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