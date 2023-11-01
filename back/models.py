from django.db import models

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

  

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    mail = models.EmailField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"ID => {self.id}, Name => {self.name},Phone => {self.phone_number}, Mail => {self.mail} ,Address => {self.address}"

