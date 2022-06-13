from django.urls import *
from .views import *


urlpatterns = [
    path('',indexListView.as_view(), name='index'),
    path('brand.html', brand),
    path('contact.html', contact),
    path('about.html', about),
    path('main', main, name='main'),
    path('index', index, name='index'),
    path('Brand/', BrandListView.as_view(), name='Brand'),
    path('Brand/add', BrandCreateView.as_view(), name='Brand-add'),
    path('Brand/change/<int:pk>', BrandUpdateView.as_view(), name='Brand-change'),
    path('Brand/delete/<int:pk>',
         BrandDeleteView.as_view(), name='Brand-delete'),
    path('Company/',  CompanyListView.as_view(), name='Company'),
    path('Company/add',  CompanyCreateView.as_view(), name='Company-add'),
    path('Company/change/<int:pk>',  CompanyUpdateView.as_view(), name='Company-change'),
    path('Company/delete/<int:pk>',
         CompanyDeleteView.as_view(), name='Company-delete'),
    path('Fps/',  FpsListView.as_view(), name='Fps'),
    path('Fps/add',  FpsCreateView.as_view(), name='Fps-add'),
    path('Fps/change/<int:pk>',  FpsUpdateView.as_view(), name='Fps-change'),
    path('Fps/delete/<int:pk>',
         FpsDeleteView.as_view(), name='Fps-delete'),
    path('sistem/',  sistemListView.as_view(), name='sistem'),
    path('sistem/add',  sistemCreateView.as_view(), name='sistem-add'),
    path('sistem/change/<int:pk>',  sistemUpdateView.as_view(), name='sistem-change'),
    path('sistem/delete/<int:pk>',
         sistemDeleteView.as_view(), name='sistem-delete'),

    path('Phone/', PhoneListView.as_view(), name='phones'),
    path('Phone/add', PhoneCreateView.as_view(), name='phone-add'),
    path('Phone/change/<int:pk>',
         PhoneUpdateView.as_view(), name='phone-change'),
    path('phone/delete/<int:pk>',
     PhoneDeleteView.as_view(), name='phone-delete'),

    ] 
  
