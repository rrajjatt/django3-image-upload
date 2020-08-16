from django.shortcuts import render,redirect
from myapp.forms import *
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def add_product(request):
    if request.method == 'GET':
        form = ProductDetailForm()
        return render(request,'myapp/add_product.html',{'form':form})
    else:
        form = ProductDetailForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'myapp/add_product.html',{'form':form,'error':'error'})

def product_list(request):
    result = ProductDetail.objects.all()
    return render(request,'myapp/product_list.html',{'result':result})

def product_detail(request,id):
    result = ProductDetail.objects.get(id=id)
    if request.method=="GET":
        return render(request,'myapp/product_detail.html',{'result':result})