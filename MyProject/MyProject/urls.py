from django.contrib import admin
from django.urls import path
from api_basic import views
from basic_api import views as cl
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('article/<int:pk>/', views.article_detail,name='detail'),
    # path('article/', views.article,name='articles'),
    path('articleapi/', views.article_api,name='articleapi'),
    path('clarticleapi/', cl.ArticleAPI.as_view(),name='clarticleapi'),
]
