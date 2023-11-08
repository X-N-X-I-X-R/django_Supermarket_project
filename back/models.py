from django.db import models 
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    img = models.ImageField(upload_to='product_images/')
   


    def __str__(self):
      return f"{self.name} = {self.price}$ "

  



class Customer_orders(models.Model):
    id = models.AutoField(primary_key=True)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    createdTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user  

class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Customer_orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    item_price = models.FloatField()
    
    def subtotal(self):
        return self.quantity * self.item_price

    def __str__(self):
        return f"Order Item {self.id} - {self.product.name}"

