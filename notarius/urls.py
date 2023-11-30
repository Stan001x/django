from django.urls import path
from .views import add_item, update_item, delete_item, ReportListView, ReportDetailView, ReportDeleteView

app_name = "notarius"

urlpatterns = [
    #/notarius/
    #path('', index, name="index"),
    path('', ReportListView.as_view(), name="index"),
    path('<int:pk>/', ReportDetailView.as_view(), name="report"),
    path('additem/', add_item, name="add_item"),
    path('updateitem/<int:my_id>/', update_item, name="update_item"),
    path('deleteitem/<int:pk>/', ReportDeleteView.as_view(), name="delete_item")
]
