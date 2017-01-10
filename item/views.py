from django.shortcuts import render
from django.views.generic import *
from .models import Item
from cart.models import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.
class Item_list(ListView):
    model = Item
    template_name = 'item/home.html'
    #context_object_name = 'item_list'
   # def get_context_data(self, **kwargs):
    ##   context['now'] = timezone.now()
      #  return context
    def get_queryset(self):
        return Item.objects.all()
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Item_list, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user=self.request.user
        Item_in_cart=Cart.objects.filter(user=user)
        if user :
                context['cart_items'] = cart_items(self.request)
        return context

@login_required
def cart_items(request):
    user=request.user.id
    n=Cart.objects.filter(user=user).count()
    return n
class Item_detail(DetailView):
    model = Item
    template_name = 'Item/item_detail.html'
    context_object_name = 'item_obj'