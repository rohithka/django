from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from products.models import Product_List

from products import views
# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):
    	product = Product_List.objects.all()
    	stu = {
    		"product":product
    	}
    	print(product.query)
    	return render(request, 'index.html',stu)


class Shop(View):

    def get(self, request, *args, **kwargs):
    	product = Product_List.objects.all()
    	stu = {
    		"product":product
    	}
    	print(product.query)
    	return render(request, 'shop-grid.html',stu)


            

	

	
