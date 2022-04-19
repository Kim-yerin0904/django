from django.contrib import admin
from django.urls import path, include
from goodplace import views

app_name = 'goodplace'

urlpatterns = [
    path('list/', views.list_map, name='list_map'),
    path('<int:matzip_id>/detail/', views.detail, name='detail'),
    path('mypage/', views.mypage, name='mypage'),
    path('review/<int:matzip_id>/', views.reviewP, name='review_page'),
    path('review_write/<int:matzip_id>/', views.reviewwrite, name='review_write'),
]