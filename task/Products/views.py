from django.shortcuts import render
from.models import *
from datetime import datetime
created_at=''
name=''
price=''
weight=''
def page(request):
    return render(request,'product.html')
def fetch_product(request):
    global created_at,name,price,weight
    product = Products()
    if request.method == 'POST':
        product.name = request.POST.get('pname')
        product.price = request.POST.get('price')
        product.weight = request.POST.get('weight')
        product.created_at = datetime.now()
        product.updated_at = datetime.now()
        product.save()
        name = product.name
        price = product.price
        weight = product.weight
        created_at = product.created_at
        updated_at = product.updated_at
        return render(request,'product_page.html',{'name':name,'price':price,'weight':weight,'created_at':created_at,'updated_at':updated_at}
        )

def update_product(request):
    global created_at,name,price,weight
    if request.method=="POST":
        product = Products.objects.get(name=name)
        if request.POST.get('price'):
            product.price = request.POST.get('price')
        if request.POST.get('weight'):
            product.weight = request.POST.get('weight')
        product.updated_at = datetime.now()
        product.save()
        price = product.price
        weight = product.weight

        updated_at = product.updated_at
        return render(request,'product_page.html',{'name':name,'price':price,'weight':weight,'created_at':created_at,'updated_at':updated_at})


def product_update(request):
    product = Products.objects.all()
    return render(request,'update_product.html',{'product':product})
def update1(request,id):
    global name,created_at
    name = id
    post = Products.objects.get(name=name)
    name = post.name
    price = post.price
    weight = post.weight
    created_at =post.created_at
    updated_at = post.updated_at
    return render(request,'product_page.html',{'name':name,'price':price,'weight':weight,'created_at':created_at,'updated_at':updated_at})
# Create your views here.
def back_product(request):
    return render(request, 'product.html',)



