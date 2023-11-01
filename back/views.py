
from rest_framework.decorators import api_view,permission_classes #! הוספת קלאס הרשאות 
from rest_framework.response import Response
from .models import Product,Category,Customer
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated #! הוספת הרשאות ושימוש בטוקן 
from django.contrib.auth.models import User #! גישה למודל קיים בטבלה של ג׳אנגו 



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def manage_member(request):
      print(request.user) # מדפיס את שם המשתמש שנכנס לתוכנה 
      return Response({"secret":"this is my secret key"})   

@api_view(["POST"])
def manage_register(request):
      x= User.objects.create_superuser(username="itay" ,password= "123")
      return Response  (f'status: success, content: Register, name: {x}')

@api_view(["GET", "POST", "PUT", "DELETE"])
def manage_products(request, product_id=None):
    if request.method == "GET":
        if product_id is not None:
            # Retrieve a specific product by ID
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            # Retrieve a list of products
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    elif request.method == "POST":
        # Create a new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        if product_id is not None:
            # Update an existing product
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        if product_id is not None:
            # Delete a product by ID
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST", "PUT", "DELETE"])
def manage_category(request, category_id=None):
    if request.method == "GET":
        if category_id is not None:
            # Retrieve a specific category by ID
            category = Category.objects.get(id=category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        else:
            # Retrieve a list of categories
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)

    elif request.method == "POST":
        # Create a new category
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        if category_id is not None:
            # Update an existing category
            category = Category.objects.get(id=category_id)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        if category_id is not None:
            # Delete a category by ID
            category = Category.objects.get(id=category_id)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST", "PUT", "DELETE"])
def manage_customers(request, customer_id=None):
    if request.method == "GET":
        if customer_id is not None:
            # Retrieve a specific customer by ID
            customer = Customer.objects.get(id=customer_id)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        else:
            # Retrieve a list of customers
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)

    elif request.method == "POST":
        # Create a new customer
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        if customer_id is not None:
            # Update an existing customer
            customer = Customer.objects.get(id=customer_id)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        if customer_id is not None:
            # Delete a customer by ID
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)