from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
#

urlpatterns=[
  path('',views.news_today,name = 'newsToday'),
  re_path('archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews'),
  path('search/', views.search_results, name='search_results'),
  path('article/(\d+)',views.article,name ='article'),
  path('accounts/',include('registration.backends.simple.urls')),
  path('tinymce/', include('tinymce.urls')),
  path('new/article', views.new_article, name='new-article'),
]


if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)