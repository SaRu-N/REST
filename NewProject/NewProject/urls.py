from django.contrib import admin
from django.urls import path
from model_api import views
from api import views as api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clarticleapi/', views.ArticleAPI.as_view(),name='clarticleapi'),
    path('articleapi/', api.hello_world,name='articleapi'),
]
