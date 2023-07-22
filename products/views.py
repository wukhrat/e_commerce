from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from products.forms import ProductReviewForm
from products.models import Product, ProductReview


class ProductView(View):
    def get(self, request):
        products = Product.objects.all().order_by("id")
        search_query = request.GET.get("q", "")
        if search_query:
            products = products.filter(title__icontains=search_query)
        page_size = request.GET.get("page_size", 4)
        paginator = Paginator(products, page_size)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        return render(request, "products/list.html", {"page_obj": page_obj,
                                                      "search_query": search_query})  # bu qolda yozilgan tepadagi esa generic view bilan ozshash


class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        review_form = ProductReviewForm()
        return render(request, "products/detail.html",
                      {"product": product,
                       "review_form": review_form})  # bu qolda yozilgan tepadagi esa generic view bilan


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        product = Product.objects.get(id=id)
        review_form = ProductReviewForm(data=request.POST)

        if review_form.is_valid():
            ProductReview.objects.create(
                product=product,
                user=request.user,
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse("products:detail", kwargs={"id": product.id}))

        return render(request, "products/detail.html",
                      {"product": product, "review_form": review_form})


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, product_id, review_id):
        product = Product.objects.get(id=product_id)
        review = product.productreview_set.get(id=review_id)
        review_form = ProductReviewForm(instance=review)

        return render(request, "products/edit_review.html",
                      context={"product": product, "review": review, "review_form": review_form})

    def post(self, request, product_id, review_id):
        product = Product.objects.get(id=product_id)
        review = product.productreview_set.get(id=review_id)
        review_form = ProductReviewForm(instance=review, data=request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect(reverse("products:detail", kwargs={"id": product.id}))

        return render(request, "products/edit_review.html",
                      context={"product": product, "review": review, "review_form": review_form})


class ConfirmDeleteView(LoginRequiredMixin, View):
    def get(self, request, product_id, review_id):
        product = Product.objects.get(id=product_id)
        review = product.productreview_set.get(id=review_id)
        return render(request, "products/confirm_delete_review.html", {"product": product, "review": review})


class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, product_id, review_id):
        product = Product.objects.get(id=product_id)
        review = product.productreview_set.get(id=review_id)

        review.delete()
        messages.success(request, "you have successfully deleted review")

        return redirect(reverse("products:detail", kwargs={"id": product.id}))
