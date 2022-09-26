from django.urls import path
from . import views


urlpatterns = [
    # path('',views.LoginPage.as_view(),name='login'),
    path('',views.HomePage.as_view(),name='home'),
    path('logout/',views.logout,name='logout'),
    path('table/',views.Table.as_view(),name='table'),
    path('billing/',views.Billing.as_view(),name='billing'),
    path('notification/',views.Notification.as_view(),name='notification'),
    path('user_details/',views.User.as_view(),name='user'),
    path('stocks_details/',views.Stocks.as_view(),name='stocks'),
    path('adduser/',views.AddUser.as_view(),name='adduser'),
    path('usertable/',views.UserTable.as_view(),name='usertable'),



]

