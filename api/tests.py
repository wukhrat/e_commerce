from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
#
# from products.models import Product, ProductReview
# from users.models import CustomUser
#
#
# class ProductReviewAPITestCase(APITestCase):
#     def setUp(self) -> None:  # darsda none yoq edi
#         self.user = CustomUser.objects.create(username="shuhrat", first_name="ilhom")
#         self.user.set_password("somepass")
#         self.user.save()
#         self.client.login(username="shuhrat", password="somepass")
#
#     def test_product_review_detail(self):
#         product = Product.objects.create(title="product", description="description3", price=1234, category="kabel")
#         product_review = ProductReview.objects.create(product=product, user=self.user, comment="good product")
#
#         response = self.client.get(reverse('api:review-detail', kwargs={"id": product_review.id}))

        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data['id'], product_review.id)
        # self.assertEqual(response.data['comment'], "good product")
        # self.assertEqual(response.data['product']['id'], product_review.product.id)
        # # self.assertEqual(response.data['category'], "kabel")
        # self.assertEqual(response.data['product']['title'], "product")
        # self.assertEqual(response.data['product']['description'], "description3")
        # self.assertEqual(response.data['product']['price'], 1234)
        # self.assertEqual(response.data['user']['id'], self.user.id)
        # self.assertEqual(response.data['user']['first_name'], 'ilhom')
        # self.assertEqual(response.data['user']['username'], "shuhrat")
    #
    # def test_delete_review(self):
    #     product = Product.objects.create(title="product", description="description3", price=1234)
    #     product_review = ProductReview.objects.create(product=product, user=self.user, comment="good product")
    #
    #     response = self.client.delete(reverse('api:review-detail', kwargs={"id": product_review.id}))
    #     self.assertEqual(response.status_code, 204)
    #     self.assertFalse((ProductReview.objects.filter(id=product_review.id).exists()))
    #
    # def test_patch_review(self):
    #     product = Product.objects.create(title="product", description="description3", price=1234)
    #     product_review = ProductReview.objects.create(product=product, user=self.user, comment="good product")
    #
    #     response = self.client.patch(reverse('api:review-detail', kwargs={"id": product_review.id}), data={"price": 1234})
    #
    #     product_review.refresh_from_db()
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(product_review.price, 1234)
    #
    # def test_put_review(self):
    #     product = Product.objects.create(title="product", description="description3", price=1234)
    #     product_review = ProductReview.objects.create(product=product, user=self.user, price=1234, comment="good product")
    #
    #     response = self.client.put(reverse('api:review-detail', kwargs={"id": product_review.id}),
    #                                data={"price": 1234, "comment": "norm product", "user_id": self.user.id,
    #                                      'product': product.id})
    #     product_review.refresh_from_db()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(product_review.price, 1234)
    #     self.assertEqual(product_review.comment, "norm product")
    #
    # def test_create_review(self):
    #     product = Product.objects.create(title="product", description="description3", price=1234)
    #     data = {
    #         "price": 2,
    #         "comment": "bad product",
    #         "user_id": self.user.id,
    #         "product": product.id
    #     }
    #
    #     response = self.client.post(reverse("api:review-list"), data=data)
    #     product_review = ProductReview.objects.get(product=product)
    #
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(product_review.price, 2)
    #     self.assertEqual(product_review.comment, 'bad product')
    #
    # def test_book_review_list(self):
    #     user_two = CustomUser.objects.create(username="shuhrat2", first_name="ilhom2")
    #     product = Product.objects.create(title="product", description="description3", price=1234)
    #     product_review = ProductReview.objects.create(product=product, user=self.user, price=5, comment="good product")
    #     br_two = ProductReview.objects.create(product=product, user=user_two, price=3, comment="not good product")
    #
    #     response = self.client.get(reverse("api:review-list"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.data['results']), 2)
    #     self.assertEqual(response.data['count'], 2)
    #     self.assertIn('next', response.data)
    #     self.assertIn('previous', response.data)
    #
    #     self.assertEqual(response.data['results'][0]['id'], br_two.id)
    #     self.assertEqual(response.data['results'][0]['price'], br_two.price)
    #     self.assertEqual(response.data['results'][0]['comment'], br_two.comment)
    #     self.assertEqual(response.data['results'][1]['id'], product_review.id)
    #     self.assertEqual(response.data['results'][1]['price'], product_review.price)
    #     self.assertEqual(response.data['results'][1]['comment'], product_review.comment)
