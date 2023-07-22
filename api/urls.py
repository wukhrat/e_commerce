from django.urls import path
from api.views import ProductReviewDetailApiView, ProductReviewsApiView

app_name = "api"
urlpatterns = [
    path("reviews/", ProductReviewsApiView.as_view(), name="review-list"),
    path("reviews/<int:id>/", ProductReviewDetailApiView.as_view(), name="review-detail"),
]