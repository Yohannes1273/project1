from django.urls import path
from . import views

urlpatterns = [
    path("",views.index2,name="index2"),
    path("add2/", views.add2, name="add2"),
    # path("add2/", views.add2, name="add2")
]