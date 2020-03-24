from django.urls import path
from .views import article_list, article_detail, ArticleAPIView

urlpatterns = [
    path('api/list', article_list),
    path('api/article', ArticleAPIView.as_view()),
    path('api/list/<int:pk>/', article_detail)
]
