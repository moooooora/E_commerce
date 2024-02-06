from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Max,Min,Q
from category.models import Category
from cart.views import _cart_id
from cart.models import CartItem
from .models import Product
from .filters import ProductFiilter
# Create your views here.

def store(request,slug=None):
    
    # price = request.GET['hun']
    # products = Product.objects.all().filter()
    # my_filter = ProductFiilter(request.GET,queryset=products)
    # products = my_filter.qs
    
    price_min = Product.objects.all().aggregate(Min('price'))
    price_max = Product.objects.all().aggregate(Max('price'))

    if slug !=None:
        category = get_object_or_404(Category,slug=slug)
        products = Product.objects.filter(category=category,is_available=True)
        products_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        products_count = products.count()
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
        'products_count' : products_count,
    }
    return render(request,'store/store.html',context)

def product_detail(request,slug,product_slug):
    try:
        category = get_object_or_404(Category,slug=slug)
        product = Product.objects.get(category=category,slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=product).exists()
        
        
    except Exception as e:
        return e

    context = {
        'product' :product,
        'in_cart' :in_cart,
    }    

    return render(request,'store/product_detail.html',context)

def love_page(request):

    return render(request,'store/love.html')

def search(request):
    products = None
    products_count = 0
    if 'keywords' in request.GET:
        keyword = request.GET['keywords']
        if keyword:
            products = Product.objects.order_by('-created_at').filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword) |Q(category__category_name__icontains=keyword))
            products_count = products.count()
    context = {
       'products' : products ,
       'products_count' : products_count,
    }
    return render(request,'store/search.html',context)

