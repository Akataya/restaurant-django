from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleList.as_view(), name="article-list"),
    path('<int:pk>/', views.ArticleDetail.as_view(), name="article-detail"),
    path('tags=<slug:tag>/', views.articles_by_tag, name='articles-by-tag'),
    path('category=<slug:category>/', views.articles_by_category, name='articles-by-category'),
]