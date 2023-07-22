from django.test import TestCase
from django.urls import reverse
from products.models import Product
from users.models import CustomUser


class BooksTestCase(TestCase):
    # def test_no_books(self):
    #     response = self.client.get(reverse("products:list"))
    #     self.assertContains(response, "No product found.")

    def test_book_list(self):
        product1 = Product.objects.create(title="product1", description="description1", price=12)
        product2 = Product.objects.create(title="product2", description="description2", price=343)
        product3 = Product.objects.create(title="product3", description="description3", price=343)

        response = self.client.get(reverse("products:list") + "?page_size=2")

        product = Product.objects.all()

        for p in [product1, product2]:
            self.assertContains(response, p.title)
        self.assertNotContains(response, product3.title)
        response = self.client.get(reverse("products:list") + "?page=2&page_size=2")

        self.assertContains(response, product3.title)