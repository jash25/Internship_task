from django.urls import path
from . import views
urlpatterns = [

path('', views.page),
    path('product/',views.fetch_product,name='product'),
    path('update_post/',views.update_product,name='update_product'),
    path('product_update/',views.product_update,name='product_update'),
    path('update_product1/<str:id>',views.update1,name='update_product1'),
    path('back_product/',views.back_product,name='back_product')
]