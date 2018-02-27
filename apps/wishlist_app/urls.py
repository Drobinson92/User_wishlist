from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add', views.add),
    url(r'^save_item', views.save_item),
    url(r'^wishlist_add/(?P<item_id>\d+)', views.wishlist_add),
    url(r'^wishlist_remove/(?P<item_id>\d+)', views.wishlist_remove),
    url(r'^wishlist_delete/(?P<item_id>\d+)', views.wishlist_delete),
    url(r'^display/(?P<item_id>\d+)', views.display),
    url(r'^', views.index),
]