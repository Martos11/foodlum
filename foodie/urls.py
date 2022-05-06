from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('meals',views.meals, name='meals'),
    path('searched',views.searched, name='searched'),
    path('details/<str:id>/<slug:slug>',views.details, name='details'),
    #the slug here is added just to show the name of the single pages on the browser
    path('variety/<str:id>/<slug:slug>',views.variety,name='variety'),
    path('loginform', views.loginform, name='loginform'),
    path('register',views.register, name = 'register'),
    path('logoutfunc',views.logoutt, name="logoutfunc"),
    path('contact', views.contact, name='contact'),
    path('profile',views.profile, name='profile'),
    path('addtocart', views.addtocart, name = 'addtocart'),
    path('cart', views.cart, name = 'cart'),
    path('remove_item', views.remove_item, name = 'remove_item'),
    path('checkout', views.checkout, name = 'checkout'),
    path('profile_update', views.profile_update, name = 'profile_update'),
    path('paidorder', views.paid_order, name='paidorder'),
    path('placeorder', views.placeorder, name='placeorder'),
    path('varieties', views.varieties, name='varieties'),
    
    
]
