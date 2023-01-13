from django.shortcuts import render
from . models import Article
import io
from . serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name='dispatch')
class ArticleAPI(View):
    def get(self,request,*args,**kwargs):
        json_data =request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            art = Article.objects.get(id=id)
            serializer=ArticleSerializer(art)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        art =Article.objects.all()
        serializer=ArticleSerializer(art,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)
    
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer =ArticleSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'data created'}
            json_data =JSONRenderer().render(res)
            return HttpResponse(json_data)
        print('ERROR')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id =pythondata.get("id")
        art=Article.objects.get(id=id)
        serializer =ArticleSerializer(art,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'data updated'}
            json_data =JSONRenderer().render(res)
            return HttpResponse(json_data)
        print('ERROR')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id =pythondata.get("id")
        art=Article.objects.get(id=id)
        art.delete()
        res= {'msg':'data deleted'}
        return JsonResponse(res,safe=False)