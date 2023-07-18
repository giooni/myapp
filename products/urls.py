from django.urls import path
from products.views import indexPageView, homepageView, WalletsView, ProductDetailView, beltsView, bagssView, accessoriesView, contactpageview

app_name = 'products'

urlpatterns = [
    path('', indexPageView.as_view(), name='index'),
    path('home/', homepageView.as_view(), name = 'home'),
    path('wallets/', WalletsView.as_view(), name='wallets'),
    path('product/<int:pk>', ProductDetailView.as_view(), name = 'product-detail'),
    path('bags/', bagssView.as_view(), name = 'bags'),
    path("accessories/", accessoriesView.as_view(), name ='accessories'),
    path("belts/", beltsView.as_view(), name='belts'),
    path('contact/', contactpageview.as_view(), name='contact'),
    
]