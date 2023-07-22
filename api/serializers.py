from rest_framework import serializers

from products.models import Product, ProductReview
from users.models import CustomUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class ProductReviewSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = ProductSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ProductReview
        fields = ('id', 'comment', 'product', 'user', 'product_id', 'user_id')