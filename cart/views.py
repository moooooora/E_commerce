from django.shortcuts import redirect, render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product,Variation
from .models import Cart,CartItem,Coupon

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    product_variations = []
    if request.method=='POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variation = Variation.objects.get(product=product,variation_category__iexact=key,variation_value__iexact=value)
                product_variations.append(variation)
            except:
                pass    

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )   
        cart.save()
    is_cart_item_exists = CartItem.objects.filter(product=product,cart=cart).exists()
    print(is_cart_item_exists)
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product,cart=cart) 
        ex_var_list = []
        id = []
        for item in cart_item:
            existing_variations = item.variations.all()
            ex_var_list.append(list(existing_variations))
            id.append(item.id)
        print(ex_var_list)    
        print(product_variations)
        new_variation = product_variations[::-1]

        print(True if new_variation in ex_var_list else False)
        if new_variation in ex_var_list :
            # increase the cart item quantity
            index = ex_var_list.index(new_variation)
            item_id = id[index]
            item = CartItem.objects.get(product=product, id=item_id)
            item.quantity += 1
            item.save()  
        else:
            item = CartItem.objects.create(product=product, quantity=1,cart=cart)      
            if len(product_variations) > 0:
                item.variations.clear()
                item.variations.add(*product_variations)
            item.save()
    else:
        cart_item = CartItem.objects.create(
            product=product,
            cart = cart,
            quantity=1,
        )      
        if len(product_variations) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variations) 
        cart_item.save()
    return redirect('cart:cart')       

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity>=1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart')    
    
def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect("cart:cart")

def cart(request,total=0,quantity=0,cart_items=None,discount=0):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price) * (cart_item.quantity)
            quantity += cart_item.quantity    
        shipping = 20
        if request.method == "POST":
            coupon = request.POST['coupon']
            get_ratio = get_object_or_404(Coupon,value=coupon)
            if get_ratio.is_active == True:
                discount = (total + shipping )  * (get_ratio.ratio/100)
                grand_total = (total + shipping ) - discount  
            else:    
                grand_total = total + shipping    
        else:    
            grand_total = total + shipping    
    except ObjectDoesNotExist:
        pass        
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'grand_total' :grand_total,
        'shipping' : shipping,
        'discount' : discount,
    }    
    return render(request,'store/cart.html',context)