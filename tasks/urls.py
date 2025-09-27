from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("add/", views.add, name="add"),
    # path("add2/", views.add2, name="add2")
]