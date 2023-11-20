from django.urls import path
from notarius import views

app_name = "notarius"

urlpatterns = [
    #/notarius/
    path('', views.index),
    path('<int:my_id>/', views.indexItem, name="report"),
]
