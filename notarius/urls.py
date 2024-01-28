from django.urls import path
from .views import update_item, delete_item, ReportListView, ReportDetailView, ReportDeleteView, main, \
    AddItem, UpdateReport

app_name = "notarius"

urlpatterns = [
    #/notarius/
    #path('', index, name="index"),
    path('notarius/', ReportListView.as_view(), name="index"),
    path('notarius/<int:pk>/', ReportDetailView.as_view(), name="report"),
    path('notarius/additem/', AddItem.as_view(), name="add_item"),
    path('notarius/updateitem/<int:my_id>/', update_item, name="update_item"),
    path('notarius/updateitem1/<int:pk>/', UpdateReport.as_view(), name="update_item1"),
    path('notarius/deleteitem/<int:pk>/', ReportDeleteView.as_view(), name="delete_item"),
    path('', main, name="main")
]
