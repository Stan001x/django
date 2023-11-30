from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Report
from django import forms


def index(request):
    items = Report.objects.all()
    context = {
        'items':items
    }
    return render(request, "notarius/notarius-main.html", context)

class ReportListView(ListView):
    model = Report
    template_name = "notarius/notarius-main.html"
    context_object_name = 'items'

def indexItem(request, my_id):
    item = Report.objects.get(id=my_id)
    context = {
        'item':item
    }
    return render(request, "notarius/report.html", context=context)

@login_required
def add_item(request):
    if request.method == "POST":
        contractnum = request.POST.get("contractnum")
        contractdate = request.POST.get("contractdate")
        clientname = request.POST.get("clientname")
        image = request.FILES['upload']
        appraiser = request.user
        item = Report(contractNumber=contractnum, conrtractDate=contractdate, clientname=clientname, image=image, appraiser=appraiser)
        item.save()
        my_id=item.pk
        return redirect(f"/notarius/{my_id}")
    return render(request, "notarius/additem.html")

def update_item(request, my_id):
    item = Report.objects.get(id=my_id)
    if request.method == "POST":
        item.contractNumber = request.POST.get("contractnum")
        item.conrtractDate = request.POST.get("contractdate")
        item.clientname = request.POST.get("clientname")
        item.image = request.FILES.get('upload', item.image)
        item.save()
    context = {'item': item}
    return render(request, "notarius/updateitem.html", context)

def delete_item(request, my_id):
    item = Report.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("/notarius/")
    context = {'item': item}
    return render(request, "notarius/deleteitem.html", context)


