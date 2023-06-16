from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    #login,logout,registartion
    path('log_in', log_in, name ='log_in'),
    path('signup/', signup, name ='signup'),
    path('log_out', log_out, name ='log_out'),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    #Blog Page
    path('', index, name ='index'),
    path('washing', washing, name ='washing'),
    path('wash_fold', wash_fold, name ='wash_fold'),
    path('dry_cleaning', dry_cleaning, name ='dry_cleaning'),
    path('shoe_laundry', shoe_laundry, name ='shoe_laundry'),
    path('saree_rooling', saree_rooling, name ='saree_rooling'),
    path('strain_removal', strain_removal, name ='strain_removal'),
    path('steam_ironing', steam_ironing, name ='steam_ironing'),
    path('carpet', carpet, name ='carpet'),
    path('toys_cleaning', toys_cleaning, name ='toys_cleaning'),
    path('services', services, name ='services'),
    #User_Interface
    path('user', user_int, name ='user'),
    path('user_cart', user_cart, name ='user_cart'),

    
]
