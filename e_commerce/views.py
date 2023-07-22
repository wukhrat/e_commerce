from django.core.paginator import Paginator
from django.shortcuts import render


from products.models import ProductReview


def landing_page(request):
    return render(request, "landing_page.html")


def home_page(request):
    book_reviews = ProductReview.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 5)
    paginator = Paginator(book_reviews, page_size)

    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)
    return render(request, "home.html", {"page_obj": page_object})