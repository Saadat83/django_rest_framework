from django.urls import path
from .views import PostListApiView, PostCreateApiView, PostDetailApiView, PostDeleteApiView, PostUpdateApiView


urlpatterns = [
    path('list/', PostListApiView.as_view(), name='list'),
    path('create/', PostCreateApiView.as_view(), name='create'),
    path('detail/<int:id>', PostDetailApiView.as_view(), name='detail'),
    path('delete/<int:id>', PostDeleteApiView.as_view(), name='delete'),
    path('update/<int:id>', PostUpdateApiView.as_view(), name='update'),
]
