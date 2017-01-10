from django.conf.urls import url
from .views import Item_list,Item_detail

urlpatterns=[

    url(r'^$',Item_list.as_view(),name='home'),
    url(r'^(?P<pk>[0-9]+)/$',Item_detail.as_view(),name='item_detail'),

]