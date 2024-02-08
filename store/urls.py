from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    
    path('',views.store,name='store'),
    path('love/',views.love_page,name='love_page'),
    path('search/',views.search,name='search'),
    path('offers/',views.offers,name='offers'),
    path('category/<slug:slug>/',views.store,name='category_slug'),
    path('category/<str:slug>/<str:product_slug>/',views.product_detail,name='product_detail'),

]

