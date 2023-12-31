
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes #! הוספת קלאס הרשאות 
from rest_framework.response import Response
from .models import OrderItems, Product,Category,Customer_orders
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated #! הוספת הרשאות ושימוש בטוקן 
from django.contrib.auth.models import User #! גישה למודל קיים בטבלה של ג׳אנגו 
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



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
        model = Customer_orders
        fields = '__all__'
        
    def create(self, validated_data):
        user = self.context['user']
        validated_data['user'] = user  # Set the user for the Customer_orders instance
        return Customer_orders.objects.create(**validated_data)


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'  
        
        
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def manage_member(request):
      print(request.user) 
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
# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['user_id']= user.id
        
        # ...
        return token
    

 

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
#!========================================        CategoryView  =================================

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
    
    
#! ----------------------------------     CustomerCreateView   -----------------------------------------------
class CustomerCreateView(APIView):
  
    def post(self, request):
        serializer = CustomerSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            order = serializer.save()
            
            # Create OrderDetails objects for each item in the list
            for item in request.data["items"]:
                print(item)
                item['order'] = order.id  # Assuming there's a foreign key to Order in OrderDetails
                serializerDt = OrderDetailsSerializer(data=item)
                if serializerDt.is_valid():
                    serializerDt.save()
                else:
                    return Response(serializerDt.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateView(APIView):
    def post(self, request):
        try:
            new_order = Customer_orders(user=request.user)
            new_order.save()
            # Assuming you are sending 'items' as a list of dictionaries
            # Each item dictionary should contain 'product_id', 'quantity', and 'item_price'
            for item_data in request.data.get('items', []):
                product_id = item_data.get('product_id')
                quantity = item_data.get('quantity')
                item_price = item_data.get('item_price')

                # Validate the product_id, quantity, and item_price
                if not product_id or not quantity or not item_price:
                    return Response({'error': 'Missing item fields: product_id, quantity, item_price'}, status=status.HTTP_400_BAD_REQUEST)
                
                # Retrieve the product instance
                product = get_object_or_404(Product, id=product_id)
   # Link the OrderItems to the new order
                order_item = OrderItems(
                    order=new_order,  # Link to the new order
                    product=product,
                    quantity=quantity,
                    item_price=item_price
                )
                order_item.save()

            return Response({'success': 'Order created successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Log the exception to the console or a file
            print(f"Error in OrderCreateView: {e}")
            # Consider sending back the exception message only in a development setting
            # In production, it's better to send a generic error message
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)