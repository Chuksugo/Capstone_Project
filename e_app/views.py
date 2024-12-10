from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import Product  # Adjust to your actual model
from rest_framework.permissions import IsAuthenticated

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        product_list = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
        return JsonResponse(product_list, safe=False)

class ProductCreateView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        new_product = Product.objects.create(
            name=data['name'],
            price=data['price']
        )
        return JsonResponse({"message": "Product created", "product_id": new_product.id})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Products list"})


