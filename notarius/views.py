from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Report
from django import forms


# def index(request):
#   page_obj = items = Report.objects.all()
#   item_name = request.Get.get('search')
#   if item_name != '' and item_name is not None:
#       page_obj = items.filter(name__icontains=item_name)
#
#   paginator = Paginator(page_obj, 2)
#   page_number = request.GET.get('page')
#   page_obj = paginator.get_page(page_number)
#    context = {'items':items, 'page_obj':page_obj}
#    return render(request, "notarius/notarius-main.html", context)

class ReportListView(ListView):
    model = Report
    template_name = "notarius/notarius-main.html"
    context_object_name = 'items'
    paginate_by = 10

# def indexItem(request, my_id):
#    item = Report.objects.get(id=my_id)
#    context = {
#        'item':item
#    }
#    return render(request, "notarius/report.html", context=context)

class ReportDetailView(DetailView):
    model = Report
    template_name = "notarius/report.html"
    context_object_name = 'item'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        context["stripe_publishable_key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context


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

class ReportDeleteView(DeleteView):
    model = Report
    success_url = reverse_lazy("notarius:index")


def main(request):
   return render(request, "notarius/main.html")


