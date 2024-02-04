from .models import CartItem

def num_of_items(request):
    items = CartItem.objects.all()
    items_count = items.count()
    return {'items_count':items_count,}