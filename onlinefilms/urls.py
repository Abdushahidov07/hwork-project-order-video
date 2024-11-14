from django.urls import path
from .views import *

urlpatterns = [
    path("", login, name="login"),
    path("home", FilmsListView.as_view(), name="home"),
    path("createfilm", FilmsCreateView.as_view(), name="createfilm"),
    path("updatefilm/<int:pk>", FilmsUpdateView.as_view(), name="updatefilm"),
    path("detailfilm/<int:pk>", FilmsDetailView.as_view(), name="detailfilm"),
    path("updatefilm/<int:pk>", FilmsDetailView.as_view(), name="updatefilm"),
    path("deletfilem/<int:pk>", FilmsDeleteView.as_view(), name="deletefilm"),
    path("createorder/<int:pk>", OrdersCreateView.as_view(), name="createorder"),
    path("allorders/", OrdersListView.as_view(), name="allorders"),
    path("detailorders/<int:pk>", OrdersDetailView.as_view(), name="detailorders"),
    path("updateorder/<int:pk>", OrdersUpdateView.as_view(), name="updateorder"),
    path("deleteorder/<int:pk>", OrdersDeleteView.as_view(), name="deleteorder"),
    path("createteatre/", TeatreCreateView.as_view(), name="createteatre"),
    path("allteatre/", TeatreListView.as_view(), name="allteatre"),
    path("detailteatre/<int:pk>", TeatreDetailView.as_view(), name="detailteatre"),
    path("updateteatre/<int:pk>", TeatreUpdateView.as_view(), name="updateteatre"),
    path("deleteteatre/<int:pk>", TeatreDeleteView.as_view(), name="deleteteatre"),
    path("createcategory/", CategoryCreateView.as_view(), name="createcategory"),
    path("allcategory/", CategoryListView.as_view(), name="allcategorys"),
    path("detailcategory/<int:pk>", CategoryDetailView.as_view(), name="detailcategory"),
    path("updatecategory/<int:pk>", CategoryUpdateView.as_view(), name="updatecategory"),
    path("deletecategory/<int:pk>", CategoryDeleteView.as_view(), name="deletecategory"),
]
