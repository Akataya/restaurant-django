from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Article, Category
from taggit.models import Tag
from django.db.models import Q


class ArticleList(ListView):
    model = Article
    term = ''
    paginate_by = 4

    # def get(self, request, *args, **kwargs):
    #     self.term = request.GET.get('term')
    #     return super(ArticleList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        term = self.request.GET.get('term')
        if term:
            context['object_list'] = Article.objects.filter(
                Q(title__icontains=term) |
                Q(content__icontains=term) |
                Q(tags__name__icontains=term)
            ).distinct()
        return context

    # Include an alternative function-based list view


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
