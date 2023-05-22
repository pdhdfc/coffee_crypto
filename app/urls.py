
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('book-table', views.book_table, name='book_table'),
    path('book_table_success_page', views.book_table_success_page, name='book_table_success_page'),
    path('about', views.about, name='about'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)