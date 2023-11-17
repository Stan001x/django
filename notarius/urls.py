from django.urls import path
from notarius import views


urlpatterns = [
    #/notarius/
    path('', views.index),
]
