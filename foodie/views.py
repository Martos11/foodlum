import uuid
import requests
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
# working on autentication section
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q

# Create your views here.

from foodie.models import *
from shopcart.models import *
from foodie.forms import *
#import registerForm from our form.py then go to the function we defined for register

def index(request):
    breakfast = Meal.objects.filter(breakfast=True, display=True).order_by('-id')[:4]
    lunch = Meal.objects.filter(lunch=True, display = True).order_by('-id')[:4]
    dinner = Meal.objects.filter(dinner=True, display = True).order_by('-id')[:4]
    varieties = Variety.objects.all()
        
    
    context = {
        'breakfast':breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'varieties':varieties
    }
    
    return render(request,'index.html',context)


def meals(request):
    # if 'itemsearch' in request.GET:
    #     searched= request.GET['itemsearch']
    #     meals = Meal.objects.filter(Q(Q(meal__icontains = searched)|Q(time__icontains = searched)))
        
    # else:
    meals = Meal.objects.all()
    
    context = {
        'meals':meals,
    }
    
    return render(request, 'meals.html',context)

def searched(request):
    if request.method=='POST':
        searched= request.POST['itemsearch']
        searched_meals = Meal.objects.filter(Q(Q(meal__icontains = searched)|Q(time__icontains = searched)))
        # searched_meals = Meal.objects.filter(meal__icontains = searched)
        
    else:
        searched_meals = Meal.objects.all()
    
    context ={
        'searched_meals':searched_meals,
    }
    
    return render(request,'searched.html', context)
        

def details(request, id, slug):
    details = Meal.objects.get(pk=id)
    
    context = {
        'details': details,
    }
    return render(request, 'details.html', context)

def variety(request, id,slug):
    #anything passed after the filter is called kwargs
    variety = Meal.objects.filter(variety_id=id)#query for single variety and its children
    single_variety = Variety.objects.get(pk=id)#query for single variety only
    
    
    context = {
        'variety':variety,
        'single_variety':single_variety,
        
        #2. the first one we defined here can be anything while the second one has to be the function we defined
        #the first one is then what we sent to our variety page so as to show the individual name
    }
    
    return render(request, 'variety.html',context)

# authenticate
def loginform(request):
    #making a post request
    if request.method == "POST":
        username2 = request.POST['username1']
        password2 = request.POST['password1']
        #authenticate is a function in django mode which access to users
        user = authenticate(request, username=username2, password = password2)
        if user:
            login(request, user)
            messages.success(request, f'Welcome {user.first_name} its good to have you here')
            return redirect("index")
        else:
            messages.info(request, 'username/password incorrect, kindly check your details, thank you')
            return redirect("loginform")
    
    
    
    return render(request,'login.html')


def logoutt(request):
    logout(request)
    return redirect('loginform')
    
#authenticate done

def register(request):
    form = RegisterForm() #instantiate the RegisterForm for a GET request
    if request.method == 'POST': #check if a post method for persisting data to the DB
        phone = request.POST['phone']
        image = request.POST['image']
        form = RegisterForm(request.POST)#instantiate the RegisterForm for a POST request
        if form.is_valid(): #ensures security checkes here meaning if data is safe it should be save to the db
            #this user can be anything sha
            user = form.save() #Save data if data is valid
            #the newuser is representing the profile model(populating the profile table upon registra)
            profile = Profile(user = user)# the first user is from the profile model saving the registrations while the second user is from this view which is holding form.save
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.phone = phone
            profile.image = image
            profile.save()
            login(request, user)
            messages.success(request, 'Registration Successful')
            return redirect('loginform')#send user in to any page you desire in ths case homepage   
        else:
            messages.warning(request, form.errors)  
            return redirect('register')
    context = {
        'varieties':varieties,
        'form':form
    }
    return render(request, 'register.html', context)


def contact(request):
    cform = ContactForm() #instantiate an empty form for a GET request
    if request.method == 'POST':
        cform = ContactForm(request.POST) #instantiate the equest for a POST request
        if cform.is_valid():
            cform.save()
            messages.success(request,'Thank you for contacting us! our customer care agent will reach you soon.')
        return redirect('index')
    
    
    context = {
        'cform': cform
    }
    return render(request, 'index.html', context)


# profile

def profile(request):
    profile = Profile.objects.get(user__username = request.user.username)
    varieties = Variety.objects.all()
    
    context ={
        'profile':profile,
        'varieties':varieties,
    }
    
    return render(request, 'profile.html', context)




def profile_update(request):
    varieties = Variety.objects.all()
    load_profile = Profile.objects.get(user__username = request.user.username)
    form = ProfileForm(instance = request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Dear {user.first_name} your profile update is successful')
            return redirect('profile')
        else:
            messages.error(request, f'Dear {user.first_name}, Kindly follow the following instructions{form.errors}, thank you')
            return redirect('password_update')
        
        
    context = {
        'varieties':varieties,
        'load_profile':load_profile,
        'form':form,
    }    
    return render(request, 'profile_update.html', context)

    
    
def addtocart(request):
    #if a user is sending in a data check for the tag by the name
    # quantity assign the value into a variable called addquantity
    # cart_code = str(uuid.uuid4())
    cartno = Profile.objects.get(user__username = request.user.username)
    cart_code = cartno.cart_code
    if request.method == "POST":
        addquantity = int(request.POST['quantity'])
        addid = request.POST['mealid']
        #making a get request and using our unique pk value
        mealid = Meal.objects.get(pk=addid)
        addspice = request.POST['how_spicey']
        #spicy is the name of the tag and whatever value that was picked would be saved into the none
        # addspicy = request.POST.get('spicy',None)
        
        cart = ShopCart.objects.filter(user__username = request.user.username, item_paid=False)
        #instantiate the cart for prospective users
        if cart: #instantiate the cart for a selected item
            #for assigning
            # more = ShopCart.objects.filter(meal_id=mealid.id,quantity=addquantity,how_spicey=addspice,user__username = request.user.username, item_paid=False).first()
            
            #for incrementing
            more = ShopCart.objects.filter(meal_id=mealid.id,user__username = request.user.username, item_paid=False).first()
            if more:
                more.quantity += addquantity
                more.how_spicey += addspice
                more.save()
                messages.success(request, "Product added to Shopcart")
                return redirect('meals')
            else: #when a cart is picked for the first time
                newitem = ShopCart()
                newitem.user = request.user
                newitem.meal = mealid
                newitem.quantity = addquantity
                newitem.how_spicey=addspice
                #importing uuid from python library
                newitem.order_no = cart[0].order_no
                newitem.item_paid = False
                newitem.save()
                messages.success(request, 'Product added ShopCart')
                return redirect('meals')
    
        else: #CREATE A CART
            newcart = ShopCart()
            newcart.user = request.user
            newcart.meal = mealid
            newcart.quantity = addquantity
            # newcart.spicy = addspicy
            newcart.how_spicey=addspice
            #importing uuid from python library
            newcart.order_no = cart_code
            newcart.item_paid = False
            newcart.save()
            messages.success(request, 'Item has been successfully added to your ShopCart!')
        
           
    return redirect('meals')

def cart(request):
    #filter by user's details which will be supplied by request
    #for everytime we are doing objects.filter or all the process will keep repeating itself
    #filter because there is possibility of pulling more than one item for a user
    #when we have a filter we aiteration in our template
    #for statement does the aiteration in the template i.e it does the pulling from the db
    cart = ShopCart.objects.filter(user__username = request.user.username,item_paid=False)
    
    subtotal = 0
    vat = 0
    total = 0
    
    for item in cart:
        if item.meal.discount:
            subtotal += item.meal.discount * item.quantity
            
        else:
            subtotal += item.meal.price * item.quantity
            
    #vat is at 7.5% of the subtotal, that is 7.5/100*subtotal
    
    vat = 0.075 * subtotal
    
    #addition of vat and subtotal gives the total value to be charged
    total = subtotal + vat
    
    context = {
        'cart':cart,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,
    }
    
    return render(request, 'cart.html', context)

#remove item from cart
def remove_item(request):
    deleteitem = request.POST['deleteitem']
    ShopCart.objects.filter(pk=deleteitem).delete()
    messages.success(request,'Item succesfully deleted from your Shopcart')
    return redirect('meals')
    


def checkout(request):
    profile = Profile.objects.get(user__username = request.user.username)
    cart = ShopCart.objects.filter(user__username = request.user.username,item_paid=False)
    
    subtotal = 0
    vat = 0
    total = 0
    
    for item in cart:
        if item.meal.discount:
            subtotal += item.meal.discount * item.quantity
            
        else:
            subtotal += item.meal.price * item.quantity
            
    #vat is at 7.5% of the subtotal, that is 7.5/100*subtotal
    
    vat = 0.075 * subtotal
    
    #addition of vat and subtotal gives the total value to be charged
    total = subtotal + vat
    
    context = {
        'profile':profile,
        'cart':cart,
        'total':total,
        # 'orderno':cart[0].order_no
    }
    return render(request, 'checkout.html',context)



def placeorder(request):
    if request.method == 'POST':
        #collect data to send to paystack
        # the api_key(application programming interface secret key) and curl(call url) will be sourced from paystack site,
        #paystack will give test secret key for testing, when you want to go live paystack will give live key
        # cburl(callback url),total, ref_num,order_num,email provided by me in my application, 
        api_key = 'sk_test_a9e6e9ff200abd335e1316a3437d5abe6b231975'
        #from paystack
        curl = 'https://api.paystack.co/transaction/initialize'
        # in the callback url i have ip address from aws
        cburl = 'http://34.204.53.200/paidorder'
        # cburl = 'http://127.0.0.1:8000/paidorder'
        ref_num = str(uuid.uuid4())
        total = float(request.POST['get_total'])*100
        cartno = Profile.objects.get(user__username = request.user.username)
        order_num = cartno.cart_code
        # order_num = request.POST['get_orderno']
        address = request.POST['address']
        phone = request.POST['phone']
        state = request.POST['state']
        user = User.objects.get(username= request.user.username)
        
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference':ref_num , 'order_number':order_num , 'amount':int(total),'callback_url':cburl, 'email':user.email, 'currency': 'NGN'}
        
        #collect data to send to paystack done
        #if currency is not stated the default is dollar
        
        #call to paystack
        
        try:
            #install request and import
            #python requests(plural) and post(lowercase)
            r = requests.post(curl, headers = headers, json = data)
        except Exception:
            messages.error(request, 'Network busy, please refresh and try again. Thank you!')
            
        else:
            transback= json.loads(r.text)
            rd_url = transback['data']['authorization_url']
            
            #take record of transaction made
            # cart = ShopCart.objects.filter(user__username = request.user.username, item_paid=False).first()
            paidorder = PaidOrder()
            paidorder.user = user
            paidorder.total = total/100
            paidorder.cart_no = order_num
            paidorder.payment_code = ref_num
            paidorder.paid_item = True
            paidorder.first_name = user.first_name
            paidorder.last_name = user.last_name
            paidorder.save()
            
            
            shipping = Shipping()
            shipping.user = user
            shipping.shipping_no = order_num
            shipping.paid_cart = True
            shipping.fname = user.first_name
            shipping.lname = user.last_name
            shipping.address = address
            shipping.phone =  phone
            shipping.state = state
            shipping.save()
            #take record of transaction made done
            
            return redirect(rd_url)
        
        #call to paystack done, when transaction is successful it redirects to the callback page
        
    #if transactins error occurs it redirect to checkout
    return redirect('checkout')

def varieties(request):
    varieties = Variety.objects.all()
    
    context ={
        'varieties':varieties
    }
    return render(request, 'varieties.html',context)
            
            
        





def paid_order(request):
    # http://127.0.0.1:2000/paidorder
    profile = Profile.objects.get(user__username = request.user.username)
    cart = ShopCart.objects.filter(user__username = request.user.username,item_paid=False)
    for item in cart:
        item.item_paid = True
        item.save()
        
        
    context ={
        'profile':profile
    }
        
    
    return render(request, 'paidorder.html', context)
    
    
    # def password_update(request):
    #     varieties = Variety.objects.all()
    #     load_profile = profile.objects.get(user__username = request.user.username)
    #     form = PasswordChangeForm(rquest.user)
    #     if request.method == 'POST':
    #         form = PasswordChangeForm(request.user,request.POST)
    #         if form.is_valid():
    #             user = form.save()
    #             update_session_auth_hash(request, user)
    #             messages.success(request, f'Dear {user.first_name} your request for password change is successful!')
    #             return redirect('password_update')
            
    #     context = {
    #         'varieties':varieties,
    #         'load_profile':load_profile,
    #         'form':form,    
    #     }
        
    #     return render(request, 'password_update.html', context)
    
    