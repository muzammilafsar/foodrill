from django.conf.urls import url
from .views import Cart_List
urlpatterns=[
    url(r'^$',Cart_List.as_view(),name='cart')
]
