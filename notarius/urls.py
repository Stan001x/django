from django.urls import path
from .views import index, indexItem, add_item, update_item, delete_item, ReportListView

app_name = "notarius"

urlpatterns = [
    #/notarius/
    #path('', index, name="index"),
    path('', ReportListView.as_view(), name="index"),
    path('<int:my_id>/', indexItem, name="report"),
    path('additem/', add_item, name="add_item"),
    path('updateitem/<int:my_id>/', update_item, name="update_item"),
    path('deleteitem/<int:my_id>/', delete_item, name="delete_item")
]
