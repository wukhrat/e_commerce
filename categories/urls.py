from django.urls import path
from categories.views import CategoryDetailView, CategoryCableView, \
    CategoryElectricalView, CategoryRozetkiView
app_name = "categories"
urlpatterns = [
    path("", CategoryDetailView.as_view(), name="category-list"),
    path("kabel/", CategoryCableView.as_view(), name='cable'),
    path("electrical/", CategoryElectricalView.as_view(), name="electrical"),
    path("rozetki/", CategoryRozetkiView.as_view(), name="rozetki")
]