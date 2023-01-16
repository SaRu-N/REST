from rest_framework import serializers
from .models import Article
from datetime import date

# validators
def starts_with_s(value):
    if value[0].lower()!='s':
        raise serializers.ValidationError('Must Start with s')
class ArticleSerializer(serializers.Serializer):
    title =serializers.CharField(max_length=100)
    author =serializers.CharField(max_length=100,validators=[starts_with_s])
    email =serializers.EmailField()
    date = serializers.DateField()

    def create(self,validated_data):
        return Article.objects.create(**validated_data)
    def update(self,instance,validate_data):
        instance.title =validate_data.get('title',instance.title)
        instance.author =validate_data.get('author',instance.author)
        instance.email =validate_data.get('email',instance.email)
        instance.date =validate_data.get('date',instance.date)
        instance.save()
        return instance
    # Field level Validation
    def validate_date(self,value):
        if value >= date.today():
            raise serializers.ValidationError('Date must be of past')
        return value
    # object level validation
    def validate(self,data):
        te=data.get('title')
        auth=data.get('author')
        if te.lower()=='java' and auth.lower()!='teacher':
            raise serializers.ValidationError('Author must be Teacher')
        return data