from django.test import TestCase, Client

from shop.models import Product, Promocode, PromocodeProduct
from shop.views import PurchaseCreate

class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)



class ProductListViewTest(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(name='Product 1', price=100)
        self.product2 = Product.objects.create(name='Product 2', price=200)
        self.promocode = Promocode.objects.create(code='test')

        PromocodeProduct.objects.create(product=self.product1, promocode=self.promocode)

    def test_product_list_view_with_promocode(self):
        response = self.client.get('/products' + '?code=test', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)

    def test_product_list_view_without_promocode(self):
        response = self.client.get('/products', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)

    def test_ajax_accessibility(self):
        response = self.client.get('/products/', {'code': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')