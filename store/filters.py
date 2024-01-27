import django_filters
from .models import Product

class ProductFiilter(django_filters.FilterSet):
    price = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    class Meta:
        model = Product
        fields = ['price',]
