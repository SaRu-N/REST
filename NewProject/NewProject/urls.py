from django.contrib import admin
from django.urls import path
from model_api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clarticleapi/', views.ArticleAPI.as_view(),name='clarticleapi'),
]
