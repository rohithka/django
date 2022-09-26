from django.shortcuts import render
from .models import Product_List
from .forms import MyForm

# Create your views here.




def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'add_product.html', {'form': form})
