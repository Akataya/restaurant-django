from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_comments.moderation import CommentModerator, moderator


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    # content = RichTextField()
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='articles/', default="default_article.jpg")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article-detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


# Comments moderation from django_comments
class ArticleModerator(CommentModerator):
    email_notification = True


moderator.register(Article, ArticleModerator)