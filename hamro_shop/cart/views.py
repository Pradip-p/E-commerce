from django.shortcuts import render, redirect
from .cart import Cart
from shop.models import Product

from django.contrib.auth.decorators import login_required

import requests
import json 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

@login_required
def card_display(request):
 
    cart = Cart(request)
    
    # Passing the object from the views to templates 
    
    contex  = {
        "cart": cart
    }
    return render(request, 'shop/cart.html', contex)

def add_to_cart(request,id):
    if request.method == "POST":
        # print(request.session['product_cart'])
        product = Product.objects.get(id=id)
        quantity = request.POST["quantity"]
        # quantity = int(quantity)
        if not quantity:
            quantity = 1
             
        cart = Cart(request)
        cart.add(product,quantity)
        

        return redirect('/')
@login_required
def update_cart(request, id):
    context ={}
    if request.method =="POST":
        data = request.POST
        quantity = data['quantity']
        cart = Cart(request)
        cart.update(quantity, id)
        
        context = {
            'cart':cart
            }

    return render(request,'shop/cart.html',context)

@login_required
def delete_cart(request,id):
    cart = Cart(request)
    cart.delete(id)
    context = {
        'cart':cart
        }
    return render(request,'shop/cart.html',context)
        
@csrf_exempt
@login_required
def verify_payment(request):
   data = request.POST
   product_id = data['product_identity']
   token = data['token']
   amount = data['amount']

   url = "https://khalti.com/api/v2/payment/verify/"
   payload = {
   "token": token,
   "amount": amount
   }
   headers = {
   "Authorization": "Key test_secret_key_56f7c4dd57a945c9af2edeeb56f7c0af"
   }
   

   response = requests.post(url, payload, headers = headers)
   
   response_data = json.loads(response.text)
   status_code = str(response.status_code)

   if status_code == '400':
      response = JsonResponse({'status':'false','message':response_data['detail']}, status=500)
      return response

   import pprint 
   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(response_data)
   
   return JsonResponse(f"Payment Done !! With IDX. {response_data['user']['idx']}",safe=False)