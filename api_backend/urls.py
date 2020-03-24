from django.urls import path
from .views import *

urlpatterns = [
    path('api/list', article_list),
    path('api/article', ArticleAPIView.as_view()),
    path('api/list/<int:pk>/', article_detail),
    path('api/articles/<int:id>/', ArticleDetailsAPIView.as_view()),
    path('api/list_v2', GenericAPIView.as_view())
]
