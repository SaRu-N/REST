from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title =serializers.CharField(max_length=100)
    author =serializers.CharField(max_length=100)
    email =serializers.EmailField()
    date = serializers.DateField()

    def create(self,validated_data):
        return Article.objects.create(validated_data)
    def update(self,instance,validate_data):
        instance.title =validate_data.get('title',instance.title)
        instance.author =validate_data.get('author',instance.author)
        instance.email =validate_data.get('email',instance.email)
        instance.date =validate_data.get('date',instance.date)
        instance.save()
        return instance