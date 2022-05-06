from django.db import models
from django.contrib.auth.models import User
from foodie.models import Meal

# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    # spicy = models.CharField(max_length=50)
    order_no = models.CharField(max_length=36)
    item_paid = models.BooleanField(default=False)
    how_spicey = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        db_table = 'ShopCart'
        managed = True
        verbose_name = 'Shopcart'
        verbose_name_plural = 'Shopcarts'
    
class PaidOrder(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    total = models.FloatField()
    cart_no = models.CharField(max_length=36, blank = True, null = True)
    payment_code = models.CharField(max_length=36)
    paid_item = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.user.username      
    
    
    class Meta:
        db_table = 'PaidOrder'
        managed = True
        verbose_name = 'PaidOrder'
        verbose_name_plural = 'PaidOrders'
    

STATUS = [
    ('new','new'),
    ('pending','pending'),
    ('processing','processing'),
    ('shipping','shipping'),
    ('delivered','delivered'),
]
class Shipping(models.Model): #paid order
    #when foreign key field is added to a referencing model it means that it can get access to
    #every other fields in the referenced model
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete = models.CASCADE, blank=True, null=True)
    shipping_no = models.CharField(max_length=50)
    paid_cart = models.BooleanField(default=False)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices =STATUS, default='new', blank=True, null= True)
    admin_remark = models.CharField(max_length=250, blank=True, null=True)
    
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        db_table = ' Shipping'
        managed = True
        verbose_name = ' Shipping'
        verbose_name_plural = ' Shippings'
    
    
    
    
    
    
    
       