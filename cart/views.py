from django.shortcuts import render
from django.views.generic import *
from .models import Cart
from item.models import Item
# Create your views here.
class Cart_List(ListView):
    model = Cart
    context_object_name = 'cart_list'
    template_name = 'cart/shopping_cart.html'
    def get_queryset(self):
        user=self.request.user
        return Cart.objects.filter(user=user)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Cart_List, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user=self.request.user

       # if user :


            #context['item_list'] = item_list

        return context