from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product (models.Model):
  
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        name = models.CharField(max_length=200, null=True, blank=True)
        base = models.CharField(max_length=200, null=True, blank=True)
        dressing = models.TextField(null=True, blank=True)
        description =  models.TextField(null=True, blank=True)
        #image = 
        price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
        status = models.CharField(max_length=200, null=True, blank=True)
        countInStock = models.IntegerField(null=True, blank=True, default=0)
        createdAt = models.DateTimeField(auto_now_add=True)
        id = models.AutoField(primary_key=True, editable=False)

        def __str__(self):
          return self.name
        
class Order(models.Model):
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        paymentMethod = models.CharField(max_length=200, null=True, blank=True)
        taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
        shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
        totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
        idPaid = models.BooleanField(default=False)
        paidAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        isDelevered = models.BooleanField(default=False)
        deliveredAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        id = models.AutoField(primary_key=True, editable=False)

        def __str__(self):
          return str(self.createdAt)
        
class OrderItem(models.Model):
        product = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
        name = models.CharField(max_length=200, null=True, blank=True)
        qty = models.IntegerField(null=True, blank=True, default=0)
        price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
        image = models.CharField(max_length=200, null=True, blank=True)
        id = models.AutoField(primary_key=True, editable=False)     

        def __str__(self):
          return str(self.name)  
        
class ShippingAdress(models.Model):
        order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
        adress = models.CharField(max_length=200, null=True, blank=True)
        city = models.CharField(max_length=200, null=True, blank=True)
        postalCode = models.CharField(max_length=200, null=True, blank=True)
        country = models.CharField(max_length=200, null=True, blank=True)
        ShippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
        id = models.AutoField(primary_key=True, editable=False)     