from operator import and_
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login ,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control 
from .models import NewUserModel, addUsers
from django.contrib.auth.models import User
from .forms import addUserForm
from django.contrib import messages
from django.db.models import Q





# HOMEPAGE
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@method_decorator(login_required,name='dispatch')

class HomePage(View):

    def get(selt,request):
        
        template = 'dashboard.html'
        context = {
                'my': "",
                

                
            }
        return render(request,template,context)

        
# LOGINPAGE

class LoginPage(LoginView):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        context ={}
        context['form'] = addUsers()
        return render(request,self.template_name, context)
    def post(self, request, *args, **kwargs):
        print(request.POST['username'])
        print(request.POST['password'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        return HttpResponseRedirect(reverse('login'))
    

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'))


# table
@method_decorator(login_required,name='dispatch')

class Table(View):
    def get(self, request, *args, **kwargs):

        template = 'tables.html'
        context = {
                'data': "Table",
            }
        return render(request,template,context)


# billing
@method_decorator(login_required,name='dispatch')

class Billing(View):
    def get(self, request, *args, **kwargs):

        template = 'billing.html'
        context = {
                'data': "Billing",            
                }
        return render(request,template,context)

# Notifications
@method_decorator(login_required,name='dispatch')

class Notification(View):
    def get(self, request, *args, **kwargs):

        template = 'notifications.html'
        context = {
                'data': "Notification",
            }
        return render(request,template,context)

# Profile
@method_decorator(login_required,name='dispatch')

class User(View):
    def get(self, request, *args, **kwargs):

        template = 'user.html'
        context = {
                'data': "User Details",
            }
        return render(request,template,context)

# stocks
@method_decorator(login_required,name='dispatch')

class Stocks(View):
    def get(self, request, *args, **kwargs):

        template = 'stocks.html'
        context = {
                'data': "Stock Details",
            }
        return render(request,template,context)


# addUserForm
@method_decorator(login_required,name='dispatch')

class AddUser(View):
    template = 'user/adduser.html'
    def get(self, request, *args, **kwargs):

        form = addUserForm()
        
        context = {'form': form,
                    'data': 'Add User'}
        return render(request,self.template,context)

    def post(self, request, *args, **kwargs):
                if request.method == 'POST':
                        form = addUserForm(request.POST)
                        if form.is_valid():
                            # print(form.cleaned_data.get('nothing'))
                            form.save()
                            messages.success(request, 'Form submission successful')
                            return redirect('adduser')
                else:
                    form = addUserForm()
                    return render(request, self.template, {'form': form, 'title':'register here'})

# UserTable
@method_decorator(login_required,name='dispatch')
class UserTable(View):
    template = 'user/usertable.html'
    def get(self, request, *args, **kwargs):

        userData = NewUserModel.objects.filter(~Q(username ='admin')).values()
        print(userData)
        
        context = { 'userData':userData,
                    'data': 'User Table'}
        return render(request,self.template,context)


# def page_not_found(request,*args):
#     return render(request, 'hello.html', status=404)

        

# def logined(request):

#    username = "not logged in"
   
#    if request.method == "POST":
#       #Get the posted form
#       MyLoginForm = AdminInputForm(request.POST)
      
#       if MyLoginForm.is_valid():
#          username = MyLoginForm.cleaned_data['username']
#          password = MyLoginForm.cleaned_data['password']
#    else:
#       MyLoginForm = AdminInputForm()
		
#    return render(request, 'login.html', {"username" : username,"password" : password})

    # def post(self, request, *args, **kwargs):

    #     # mydata = Users.objects.filter(username = "admin").values()
    #     # d = list(mydata)
    #     # new = d[0]
    #     # usernamedb = new['username']
    #     # passworddb = new['password']


    #     form = AdminInputForm()

    #     if form.is_valid():
        
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
            

        
    #     return render(request=request, template_name="login.html", context={"login_form":username, "user":password})





            
    




