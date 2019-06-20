from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Article, Category
from taggit.models import Tag


class ArticleList(ListView):
    model = Article


class ArticleDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        context['all_categories'] = Category.objects.all()
        return context


def articles_by_tag(request, tag):
    articles_by_tag = Article.objects.filter(tags__name__in=[tag])
    context = {
        'object_list': articles_by_tag
    }
    return render(request, 'blog/article_list.html', context)


def articles_by_category(request, category):
    articles_by_category = Article.objects.filter(category__name=category)
    context = {
        'object_list': articles_by_category
    }
    return render(request, 'blog/article_list.html', context)
