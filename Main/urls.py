from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('items/<slug:direction>/<slug:catagory>', views.items, name='items'),
    path('items/<slug:direction>', views.items, name='items'),
    path('item/<uuid:id>', views.item, name='item'),
    path('inbox', views.inbox, name='inbox'),
]
