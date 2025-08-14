from django.urls import path
from . import views  # 현재 폴더(blog)의 views.py 불러오기

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

