from django.test import TestCase
from shop.models import Product, Purchase, Promocode, PromocodeProduct
from datetime import datetime

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="book", price="740")
        Product.objects.create(name="pencil", price="50")

    def test_correctness_types(self):                   
        self.assertIsInstance(Product.objects.get(name="book").name, str)
        self.assertIsInstance(Product.objects.get(name="book").price, int)
        self.assertIsInstance(Product.objects.get(name="pencil").name, str)
        self.assertIsInstance(Product.objects.get(name="pencil").price, int)        

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="book").price == 740)
        self.assertTrue(Product.objects.get(name="pencil").price == 50)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_book = Product.objects.create(name="book", price="740")
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_book,
                                person="Ivanov",
                                address="Svetlaya St.")

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).person, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).address, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).date, datetime)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(product=self.product_book).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(product=self.product_book).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(product=self.product_book).date.replace(microsecond=0) == \
            self.datetime.replace(microsecond=0))


class PromocodeTestCase(TestCase):
    def setUp(self):
        self.promocode = Promocode.objects.create(code="CODE")

    def test_correctness_types(self):
        self.assertIsInstance(self.promocode.code, str)
        self.assertIsInstance(self.promocode.date, datetime)

    def test_correctness_data(self):
        self.assertTrue(self.promocode.code == "CODE")
        self.assertTrue(self.promocode.date is not None)


class PromocodeProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="book", price=740)
        self.product2 = Product.objects.create(name="pencil", price=50)
        self.promocode = Promocode.objects.create(code="DISCOUNT10")
        self.promocode_product = PromocodeProduct.objects.create(
            promocode=self.promocode,
            product=self.product
        )

    def test_correctness_types(self):
        self.assertIsInstance(self.promocode_product.promocode, Promocode)
        self.assertIsInstance(self.promocode_product.product, Product)

    def test_correctness_data(self):
        self.assertTrue(self.promocode_product.promocode.code == "DISCOUNT10")
        self.assertTrue(self.promocode_product.product.name == "book")

    def test_multiple_products_for_promocode(self):
        self.promocode_product2 = PromocodeProduct.objects.create(
            promocode=self.promocode,
            product=self.product2
        )

        promocode_products = PromocodeProduct.objects.filter(promocode=self.promocode)
        self.assertEqual(promocode_products.count(), 2)
        self.assertIn(self.promocode_product2, promocode_products)

    def test_promocode_product_deletion(self):
        self.promocode_product.delete()
        self.assertEqual(PromocodeProduct.objects.count(), 0)
