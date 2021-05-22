from django.conf import settings
from shop.models import Product
from decimal import Decimal
class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart

    def add(self, product, quantity):
        
        quantity = int(quantity)
        product_id = str(product.id)
        
        """
        product_cart: {
            1: {'quantity': 2, price:300},
            2: {'quantity': 6, price:700},
            3: {'quantity': 4, price:100}
        }
        """
        if not product_id in self.cart:
            self.cart[product_id] ={"quantity":quantity, "price": str(product.price) }
            
        else:
            self.cart[product_id]["quantity"] += quantity 
            
        self.save()        

    def save(self):
        self.session.modified = True
        

        
    def list(self):
        # return self.cart
        carts = []
        for product_id in self.cart.keys():
            obj = Product.objects.get(id = product_id)
            temp_cart = {
                'id': product_id,
                'obj': obj,
                'quantity': self.cart[product_id]['quantity'],
                'price': Decimal(int(self.cart[product_id]['quantity']) * float(obj.price))
            }
            
            carts.append(temp_cart)
        return carts
    
    def get_total_amount(self):
        return sum(float(v['price'])* int(v['quantity'] ) for v in self.cart.values())
        
    def update(self,quantity,product_id):
        pid = str(product_id)
        '''
            dct = {'1':"idnesa','2':"dont knwo"}
            dct['1'] = 'fjdsfk'
        '''
        # print(self.cart)s
        self.cart[pid]['quantity'] = quantity
        self.save()
        # print(self.cart)
    def delete(self,product_id):
        pid = str(product_id)
        del self.cart[pid]
        self.save()
        
    def clearcart(self):
        del self.session[settings.CART_SESSION_KEY]
        self.save()
        