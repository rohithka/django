from django import forms
from .models import Product_List

class MyForm(forms.ModelForm):
  class Meta:
    model = Product_List
    fields = ["Product_name", "Price","Quantity","Image_Link"]
    labels = {'Product_name': "Product","Price":"Price", "Quantity": "Quantity","Image_Link": "Image link"}
