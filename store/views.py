from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Max,Min
from .models import Product
from .filters import ProductFiilter
# Create your views here.

def store(request):
    
    # price = request.GET['hun']
    # products = Product.objects.all().filter()
    # my_filter = ProductFiilter(request.GET,queryset=products)
    # products = my_filter.qs
    price_min = Product.objects.all().aggregate(Min('price'))
    price_max = Product.objects.all().aggregate(Max('price'))
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        products = Product.objects.filter(price__lte = Int_FilterPrice,is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    paginator = Paginator(products,6) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    print(price_min)
    print(price_max)
    context = {
        'products' : page_obj,
        # 'myfilter':my_filter,
        'price_min' : price_min,
        'price_max' : price_max,
        'FilterPrice':FilterPrice,
    }
    return render(request,'store/store.html',context)

def product_detail(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        
        
    except Product.DoesNotExist:
        pass

    context = {
        'product' :product,
    }    

    return render(request,'store/product_detail.html',context)


