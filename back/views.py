
from django.db import IntegrityError
from rest_framework.decorators import api_view,permission_classes #! הוספת קלאס הרשאות 
from rest_framework.response import Response
from .models import Product,Category,Customer
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated #! הוספת הרשאות ושימוש בטוקן 
from django.contrib.auth.models import User #! גישה למודל קיים בטבלה של ג׳אנגו 
from rest_framework.views import APIView


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
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"status": "error", "message": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, password=password)
        return Response({"status": "success", "message": "User registered successfully."})
    except IntegrityError:
        return Response({"status": "error", "message": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

  
#!===============================================================

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from rest_framework.permissions import IsAuthenticated

class CategoryView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):  # Make sure 'request' parameter is included
        my_model = Category.objects.all()
        serializer = CategorySerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        my_model = Category.objects.get(pk=pk)
        serializer = CategorySerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        my_model = Category.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 

class ProductView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):  # Make sure 'request' parameter is included
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomerView(APIView):
    #permission_classes = [IsAuthenticated]

    
    def get(self, request):  # Make sure 'request' parameter is included
        my_model = Customer.objects.all()
        serializer = CustomerSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CustomerSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        my_model = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        my_model = Customer.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)