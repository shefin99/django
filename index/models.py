from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    user=models.OneToOneField(User,null=True,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    digital=models.BooleanField(default=False,null=True,blank=True)
    #offers=models.BooleanField(default=False)
    image=models.ImageField(null=True,blank=True,upload_to='pics')
    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url=self.image.url
        except:
            url=' '
        return url

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.IntegerField()
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total

    
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total
    
class ShippingAddress(models.Model):
    Customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=200,null=False)
    city=models.CharField(max_length=200,null=False)
    state=models.CharField(max_length=200,null=False)
    def __str__(self):
        return self.address






    