from django.shortcuts import render
from . models import Article
from . serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
# Model Object
def article_detail(request,pk):
    a=Article.objects.get(id=pk)
    serializer =ArticleSerializer(a)
    # json_data =JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data)
# Queryset
def article(request):
    a=Article.objects.all()
    serializer =ArticleSerializer(a,many=True)
    # json_data =JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data,safe=False)
