from django.shortcuts import render
from django.db.models import Count
from category.models import Category
from store.models import Product


def home(request):

    category_counts = Category.objects.annotate(product_count=Count('product'))

    # for category in category_counts:
    #     print(category.category_name, category.product_count,'***************')


    context = {
        'categories':category_counts,
        
    }
    return render(request,'home/home.html',context)
