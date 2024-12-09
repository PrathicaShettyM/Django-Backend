# sub url.py
from django.urls import path
from . import views

# localhost:8000/chai  => will be the home of this sub url
# localhost:8000.chai/order => any new url from this suburl
urlpatterns = [
    path('', views.all_chai, name='all_home'),
    path('order/', views.order, name='order_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
]