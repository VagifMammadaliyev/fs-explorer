from django.urls import path
from explorer import views


urlpatterns = [
    path('', views.home, name='home'),
    path('save/<path:abspath>', views.save_node, name='save_node'),
    path('img/<path:img_path>', views.image, name='image'),
    path('<path:abspath>', views.node, name='node'),
]
