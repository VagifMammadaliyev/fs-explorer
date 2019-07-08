from django.urls import path
from explorer import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<path:abspath>', views.node, name='node'),
]
