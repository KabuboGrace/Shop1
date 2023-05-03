from django.contrib import admin
from django.urls import path
from ShopApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('products/',views.products, name='products'),
    path('store/',views.store, name='store'),

]