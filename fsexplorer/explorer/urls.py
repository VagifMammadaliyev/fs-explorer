from django.urls import path
from explorer import views


urlpatterns = [
    path('', views.home, name='home'),
    path('rename', views.rename_node, name='rename_node'),
    path('create/<path:abspath>', views.create_node, name='create_node'),
    path('save/<path:abspath>', views.save_node, name='save_node'),
    path('img/<path:img_path>', views.image, name='image'),
    path('video/<path:vid_path>', views.video, name='video'),
    path('<path:abspath>', views.node, name='node'),
]
