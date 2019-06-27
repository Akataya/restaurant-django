from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls', namespace='contact')),
    path('menu/', include('menu.urls', namespace='menu')),
    path('about/', include('about.urls', namespace='about')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('reservation/', include('reservation.urls', namespace='reservation')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^comments/', include('django_comments_xtd.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)