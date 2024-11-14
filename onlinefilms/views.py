from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

def login(request):
    return redirect('/accounts/login/')

class FilmsListView(LoginRequiredMixin, ListView):
    model = Films
    template_name = "home.html"
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['teatres'] = Teatre.objects.all()
        return context

class FilmsDetailView(LoginRequiredMixin, DetailView):
    model = Films
    template_name = "films.html"
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Orders.objects.filter(film=self.get_object())
        return context

class FilmsCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Films
    template_name = "createfilm.html"
    fields = ("title", "category_id", "descriptions", "tikets", "price", "teatre", "video", "img", "date_view")
    success_url = reverse_lazy('home')
    permission_required = 'hamsafar.viev_film'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class FilmsUpdateView(LoginRequiredMixin, UpdateView):
    model = Films
    template_name = "updatefilm.html"
    fields = ("title", "category_id", "descriptions", "tikets", "price", "teatre", "video", "img", "date_view")
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Films.objects.filter(created_by=self.request.user)

class FilmsDeleteView(LoginRequiredMixin, DeleteView):
    model = Films
    template_name = "deletefilm.html"
    context_object_name = 'film'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Films.objects.filter(created_by=self.request.user)

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "allcategory.html"
    context_object_name = 'categorys'

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "detailcategory.html"
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["films"] = Films.objects.filter(category_id=self.kwargs['pk'])
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "createcategory.html"
    fields = ("category_name",)
    success_url = reverse_lazy('allcategorys')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "updatecategory.html"
    fields = ("category_name",)
    success_url = reverse_lazy('allcategorys')

    def get_queryset(self):
        return Category.objects.filter(created_by=self.request.user)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "deletecategory.html"
    success_url = reverse_lazy('allcategorys')

    def get_queryset(self):
        return Category.objects.filter(created_by=self.request.user)

class TeatreListView(LoginRequiredMixin, ListView):
    model = Teatre
    template_name = "allteatre.html"
    context_object_name = 'teatres'

class TeatreDetailView(LoginRequiredMixin, DetailView):
    model = Teatre
    template_name = "detailteatre.html"
    context_object_name = 'teatre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["films"] = Films.objects.filter(teatre=self.kwargs["pk"])
        return context

class TeatreCreateView(LoginRequiredMixin, CreateView):
    model = Teatre
    template_name = "createteatre.html"
    fields = ("name_teatre", "city_id", "region_id", "street_id")
    success_url = reverse_lazy('allteatre')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TeatreUpdateView(LoginRequiredMixin, UpdateView):
    model = Teatre
    template_name = "updateteatre.html"
    fields = ("name_teatre", "city_id", "region_id", "street_id")
    success_url = reverse_lazy('allteatre')

    def get_queryset(self):
        return Teatre.objects.filter(created_by=self.request.user)

class TeatreDeleteView(LoginRequiredMixin, DeleteView):
    model = Teatre
    template_name = "deletefilm.html"
    context_object_name = 'teatre'
    success_url = reverse_lazy('allteatre')

    def get_queryset(self):
        return Teatre.objects.filter(created_by=self.request.user)

class OrdersListView(LoginRequiredMixin, ListView):
    model = Orders
    template_name = "allorders.html"
    context_object_name = 'orders'

class OrdersDetailView(LoginRequiredMixin, DetailView):
    model = Orders
    template_name = "detailorders.html"
    context_object_name = 'order'

class OrdersCreateView(LoginRequiredMixin, CreateView):
    model = Orders
    template_name = "createorder.html"
    fields = ("qvantity", "type_pay")
    success_url = reverse_lazy('allorders')

    def form_valid(self, form):
        films = Films.objects.filter(id=self.kwargs["pk"]).first()
        if films:
            form.instance.film = films
            form.instance.user_id = self.request.user
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class OrdersUpdateView(LoginRequiredMixin, UpdateView):
    model = Orders
    template_name = "updateorders.html"
    fields = ("user_id", "film", "qvantity", "type_pay")
    success_url = reverse_lazy('allorders')

    def get_queryset(self):
        return Orders.objects.filter(user_id=self.request.user)

class OrdersDeleteView(LoginRequiredMixin, DeleteView):
    model = Orders
    template_name = "deleteorders.html"
    success_url = reverse_lazy('allorders')
    context_object_name = "order"

    def get_queryset(self):
        return Orders.objects.filter(user_id=self.request.user)
