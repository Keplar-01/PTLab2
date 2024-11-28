from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')


class ProductListView(View):
    def get(self, request):
        promocode = request.GET.get('code', '')

        if promocode:
            products = Product.objects.filter(
                Q(promocodeproduct__promocode__code=promocode) | Q(promocodeproduct__isnull=True),
            )
        else:
            products = Product.objects.filter(promocodeproduct__isnull=True)

        products_data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]

        return JsonResponse({'products': products_data})
