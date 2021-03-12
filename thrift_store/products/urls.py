from django.conf.urls import url
from tutorials import views

urlpatterns = [
    url(r'^api/products$', views.product_list),
    url(r'^api/products/(?P<pk>[0-9]+)$', views.product_detail),
    url(r'^api/products/posted$', views.product_list_posted)
]
