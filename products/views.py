
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from typing import Any, Self
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from products.forms import CommentForm
from .models import Product, Comment
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

class indexPageView(TemplateView):
    template_name = "index.html"
class homepageView(TemplateView):
    template_name = 'home.html'
class contactpageview(TemplateView):
    template_name = 'contact.html'
class WalletsView(ListView):
    model = Product
    template_name = 'wallets.html'  
    context_object_name = 'products'
    paginate_by = 12
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category='wallet')  
        queryset = queryset.filter(tags__name__icontains = self.request.GET.get('q', "")).order_by("-createtime") 
        return queryset
    
    def get_absolut_url(self):
        return reverse('products:product-detail', kwargs= {"pk":self.pk})
class bagssView(ListView):
    model = Product
    template_name = 'bags.html'  
    context_object_name = 'products'
    paginate_by = 12
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category='bag')  
        queryset = queryset.filter(tags__name__icontains = self.request.GET.get('q', "")).order_by("-createtime") 
        return queryset
    
    def get_absolut_url(self):
        return reverse('products:product-detail', kwargs= {"pk":self.pk})
class beltsView(ListView):
    model = Product
    template_name = 'belts.html'  
    context_object_name = 'products'
    paginate_by = 12
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category='belt') 
        queryset = queryset.filter(tags__name__icontains = self.request.GET.get('q', "")).order_by("-createtime") 
        return queryset
    def get_absolut_url(self):
        return reverse('products:product-detail', kwargs= {"pk":self.pk})
class accessoriesView(ListView):
    model = Product
    template_name = 'accessories.html'  
    context_object_name = 'products'
    paginate_by = 12
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category='accessories')  
        queryset = queryset.filter(tags__name__icontains = self.request.GET.get('q', "")).order_by("-createtime")
        return queryset
    
    def get_absolut_url(self):
        return reverse('products:product-detail', kwargs= {"pk":self.pk})


class ProductDetailView(DetailView, CreateView):
    model = Product
    template_name = "productdetail.html"
    context_object_name = "product"
    form_class = CommentForm

    def get_success_url(self):
        product = self.get_object()
        return reverse('products:product-detail', kwargs={'pk': product.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(product=self.object)
        return context

    def form_valid(self, form):
        form.instance.product = self.get_object()
        form.instance.user = self.request.user
        return super().form_valid(form)
    


    
    


