from django.urls import path
from explorer import views


urlpatterns = [
    path('', views.home, name='home'),
    path('img/<path:img_path>', views.image, name='image'),
    path('<path:abspath>', views.node, name='node'),
]
