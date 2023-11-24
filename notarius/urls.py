from django.urls import path
from notarius import views

app_name = "notarius"

urlpatterns = [
    #/notarius/
    path('', views.index),
    path('<int:my_id>/', views.indexItem, name="report"),
    path('additem/', views.add_item, name="add_item"),
    path('updateitem/<int:my_id>/', views.update_item, name="update_item")
]
