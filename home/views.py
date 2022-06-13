
from unicodedata import name
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.db.models import Q
# # Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
# Create your views here.


class indexListView(ListView):
    template_name = 'main.html'
    context_object_name = 'phones'
    def get_queryset(self):
        url_data = self.request.GET
        q = Phone.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        if 'Company' in url_data and url_data['Company']:
            q = q.filter(
                company__title__icontains=url_data['Company'])

        if 'Brand' in url_data and url_data['Brand']:
            q = q.filter(
                brand__name__icontains=url_data['Brand'])

        if 'price' in url_data and url_data['price']:
            q = q.filter(
                price=url_data['price'])

        if 'fps' in url_data and url_data['fps']:
            q = q.filter(
                fps=url_data['fps'])

        if 'color' in url_data and url_data['color']:
            q = q.filter(color__icontains=url_data['color'])
        
        return q

def add_phones(request):
    print(request.POST)
    return render(request, "add-phones.html")


class BrandListView(ListView):
    template_name = 'Brand.html'
    context_object_name = 'Brand'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = Brand.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        return q


class BrandCreateView(CreateView):
    queryset = Brand.objects.all()
    template_name = 'Brand-add.html'
    fields = "__all__"

    success_url = '/Brand'


class BrandUpdateView(UpdateView):
    queryset = Brand.objects.all()
    template_name = 'Brand-add.html'
    fields = "__all__"
    context_object_name = 'brand'
    success_url = '/Brand'


class BrandDeleteView(DeleteView):
    queryset = Brand.objects.all()
    template_name = 'Brand-delete.html'
    fields = "__all__"

    success_url = '/Brand'


class FpsListView(ListView):
    template_name = 'Fps.html'
    context_object_name = 'Fps'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = Fps.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        return q


class FpsCreateView(CreateView):
    queryset = Fps.objects.all()
    template_name = 'Fps-add.html'
    fields = "__all__"

    success_url = '/Fps'


class FpsUpdateView(UpdateView):
    queryset = Fps.objects.all()
    template_name = 'Fps-add.html'
    fields = "__all__"
    context_object_name = 'Fps'
    success_url = '/Fps'


class FpsDeleteView(DeleteView):
    queryset = Fps.objects.all()
    template_name = 'Fps-delete.html'
    fields = "__all__"

    success_url = '/Fps'

    
class sistemListView(ListView):
    template_name = 'sistem.html'
    context_object_name = 'sistem'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = sistem.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        return q


class sistemCreateView(CreateView):
    queryset = sistem.objects.all()
    template_name = 'sistem-add.html'
    fields = "__all__"

    success_url = '/sistem'


class sistemUpdateView(UpdateView):
    queryset = sistem.objects.all()
    template_name = 'sistem-add.html'
    fields = "__all__"
    context_object_name = 'sistem'
    success_url = '/sistem'


class sistemDeleteView(DeleteView):
    queryset = sistem.objects.all()
    template_name = 'sistem-delete.html'
    fields = "__all__"

    success_url = '/sistem'



class CompanyListView(ListView):
    queryset = Company.objects.all()
    template_name = 'Company.html'
    context_object_name = 'Company'
    
    def get_queryset(self):
        url_data = self.request.GET
        q = Company.objects.all()

        if 'title' in url_data and url_data['title']:
            q = q.filter(title__icontains=url_data['title'])
        return q


class CompanyCreateView(CreateView):
    queryset = Company.objects.all()
    template_name = 'Company-add.html'
    fields = "__all__"

    success_url = '/Company'


class CompanyUpdateView(UpdateView):
    queryset = Company.objects.all()
    template_name = 'Company-add.html'
    fields = "__all__"

    success_url = '/Company'


class CompanyDeleteView(DeleteView):
    queryset = Company.objects.all()
    template_name = 'Company-delete.html'
    fields = "__all__"

    success_url = '/Company'


class PhoneListView(ListView):
    queryset = Phone.objects.all()
    template_name = 'phones.html'


    context_object_name = 'Phone'
 
    


    def get_queryset(self):
        url_data = self.request.GET
        q = Phone.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        if 'Company' in url_data and url_data['Company']:
            q = q.filter(
                company__title__icontains=url_data['Company'])

        if 'Brand' in url_data and url_data['Brand']:
            q = q.filter(
                brand__name__icontains=url_data['Brand'])

        if 'price' in url_data and url_data['price']:
            q = q.filter(
                price=url_data['price'])

        if 'fps' in url_data and url_data['fps']:
            q = q.filter(
                fps=url_data['fps'])

        if 'country' in url_data and url_data['color']:
            q = q.filter(color__icontains=url_data['color'])
        
        if 'sistem' in url_data and url_data['color']:
            q = q.filter(color__icontains=url_data['color'])

        if 'memory' in url_data and url_data['color']:
            q = q.filter(color__icontains=url_data['color'])

        if 'color' in url_data and url_data['color']:
            q = q.filter(color__icontains=url_data['color'])
            
        if 'img' in url_data and url_data['color']:
            q = q.filter(color__icontains=url_data['color'])
        return q



class PhoneCreateView(CreateView):
    queryset = Phone.objects.all()
    template_name = 'phone-add.html'
    fields = "__all__"

    success_url = '/Phone'


class PhoneUpdateView(UpdateView):
    queryset = Phone.objects.all()
    template_name = 'phone-add.html'
    fields = "__all__"

    success_url = '/Phone'


def main(request):
    bks = Phone.objects.all()

    context = {'phone': bks}
    return render(request, "main.html", context=context)


def index(request):
    bks = Phone.objects.all()

    context = {'phone': bks}
    return render(request, "index.html", context=context)




class PhoneDeleteView(DeleteView):
    queryset = Phone.objects.all()
    template_name = 'phone-delete.html'
    fields = "__all__"

    success_url = '/Phone'

def about(request):
    return render(request, "about.html")
def brand(request):
    return render(request, "brand.html")
def contact(request):
    return render(request, "contact.html")


