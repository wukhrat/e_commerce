from django.urls import path
from products.views import ProductView, ProductDetailView, AddReviewView, EditReviewView, ConfirmDeleteView, \
    DeleteReviewView
app_name = "products"
urlpatterns = [
    path("", ProductView.as_view(), name="list"),
    path("<int:id>/", ProductDetailView.as_view(), name="detail"),
    path("<int:id>/reviews/", AddReviewView.as_view(), name="reviews"),
    path("<int:product_id>/reviews/<int:review_id>/edit/", EditReviewView.as_view(), name="edit-review"),
    path("<int:product_id>/reviews/<int:review_id>/delete/confirm/", ConfirmDeleteView.as_view(), name="confirm-delete-review"),
    path("<int:product_id>/reviews/<int:review_id>/delete/", DeleteReviewView.as_view(),
         name="delete-review"),

]