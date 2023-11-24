from django.shortcuts import render
from django.http import HttpResponse
from .models import Report

def index(request):
    items = Report.objects.all()
    context = {
        'items':items
    }
    return render(request, "notarius/notarius-main.html", context)

def indexItem(request, my_id):
    item = Report.objects.get(id=my_id)
    context = {
        'item':item
    }
    return render(request, "notarius/report.html", context=context)

def add_item(request):
    if request.method == "POST":
        contractnum = request.POST.get("contractnum")
        contractdate = request.POST.get("contractdate")
        clientname = request.POST.get("clientname")
        image = request.FILES['upload']
        item = Report(contractNumber=contractnum, conrtractDate=contractdate, clientname=clientname, image=image)
        item.save()
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