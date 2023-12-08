from django.urls import path
from .views import add_item, update_item, delete_item, ReportListView, ReportDetailView, ReportDeleteView, main

app_name = "notarius"

urlpatterns = [
    #/notarius/
    #path('', index, name="index"),
    path('notarius/', ReportListView.as_view(), name="index"),
    path('notarius/<int:pk>/', ReportDetailView.as_view(), name="report"),
    path('notarius/additem/', add_item, name="add_item"),
    path('notarius/updateitem/<int:my_id>/', update_item, name="update_item"),
    path('notarius/deleteitem/<int:pk>/', ReportDeleteView.as_view(), name="delete_item"),
    path('', main, name="main")
]
