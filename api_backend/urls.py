from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('api/list', article_list),
    path('api/detail/<int:pk>/', article_detail)
]
