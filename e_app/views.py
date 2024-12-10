from django.http import JsonResponse
from django.views import View
from .models import Product  # Adjust to your actual model

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        product_list = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
        return JsonResponse(product_list, safe=False)

class ProductCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        new_product = Product.objects.create(
            name=data['name'],
            price=data['price']
        )
        return JsonResponse({"message": "Product created", "product_id": new_product.id})
