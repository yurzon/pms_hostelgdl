from django.urls import path
from . import views

urlpatterns = [
    path("", views.beds_index, name="beds_index"),
]
