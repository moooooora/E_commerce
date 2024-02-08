from .models import Offer

def offer(request):
    offers = Offer.objects.all().filter(is_active=True)
   
    return {'offers':offers,}
