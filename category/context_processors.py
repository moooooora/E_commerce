from .models import Category

def category_link(request):
    categories= Category.objects.all()

    return {'categories':categories}