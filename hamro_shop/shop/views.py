from django.shortcuts import redirect, render
from .models import Category, Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    category = Category.objects.all()
    
    
    contex={
        'products':products,
        'categorys': category,
    }
    return render(request, 'shop/index.html', contex)


def category_filter(request):
    category = Category.objects.all()
    products = Product.objects.all()
    
    if request.method == "POST":
        category_name = request.POST['category']
    
        # To get Category Id
        category_name = Category.objects.filter(name=category_name)
        category_id = category_name[0].id

        #  To prodcuts details according to the category
        products = Product.objects.filter(category_id = category_id)
        
        
        # To get all category
        category = Category.objects.all()
        contex={
        'products':products,
        'categorys': category,
        }
        return render(request, 'shop/index.html', contex)

    contex={
        'products':products,
        'categorys': category,
    }
    return render(request, 'shop/index.html', contex)
        