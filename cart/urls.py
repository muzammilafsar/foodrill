from django.conf.urls import url
from .views import Cart_List,addtocart
urlpatterns=[
    url(r'^$',Cart_List.as_view(),name='cart'),
    url(r'^addtocart$',addtocart,name='addtocart')

]
