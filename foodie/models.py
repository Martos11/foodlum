
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload

# Create your models here.
#when it comes to adding a relationship field to an existing model the default should be equal to id
#foreingkey is used to link one model to another.one field in d referencing model relating to other referenced model

class Variety(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique = True, null=False)
    #blank takes care of form validation while null takes care of db validation
    image = models.ImageField(upload_to = 'variety', default = 'variety.jpg', blank = True, null = True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'variety'
        managed = True
        verbose_name = 'Variety'
        verbose_name_plural = 'Varieties'
        
SPICEY = [
    ('Not','Not'),
    ('Mild','Mild'),
    ('Medium', 'Medium'),
    ('Hot', 'Hot'),
    ('Extra Hot', 'Extra Hot'),
]        

class Meal(models.Model):
    variety = models.ForeignKey(Variety, on_delete = models.CASCADE)
    meal = models.CharField(max_length=100)
    slug = models.SlugField(unique = True, null=False)
    menu = models.TextField()
    image = models.ImageField(upload_to = meal, default = 'meal.jpg')
    #choice is used when we have options more than two so then we can create a list or turple to make our choices
    #while boolean can only be used for just two options
    spicy = models.CharField(max_length=100, choices=SPICEY, default='Medium')
    time= models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.FloatField(blank = True, null = True)
    min_order = models.IntegerField(default=1)
    max_order = models.IntegerField(default=20)
    breakfast = models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()
    display = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now= True)
    updated = models.DateTimeField(auto_now= True)
    
    class Meta:
        db_table = 'meal'
        managed = True
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'
        

    
    
    
       