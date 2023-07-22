from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import ProductReview
from api.serializers import ProductReviewSerializers


class ProductReviewDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        product_review = ProductReview.objects.get(id=id)
        serializer = ProductReviewSerializers(product_review)

        return Response(data=serializer.data)

    def delete(self, request, id):
        product_review = ProductReview.objects.get(id=id)
        product_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        product_review = ProductReview.objects.get(id=id)
        serializer = ProductReviewSerializers(instance=product_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        product_review = ProductReview.objects.get(id=id)
        serializer = ProductReviewSerializers(instance=product_review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductReviewsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        product_reviews = ProductReview.objects.all().order_by('-created_at')

        paginator = PageNumberPagination()
        page_object = paginator.paginate_queryset(product_reviews, request)
        serializer = ProductReviewSerializers(page_object, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ProductReviewSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)