from rest_framework import serializers
from . models import Article
from datetime import date

class ArticleSerializer(serializers.ModelSerializer):
    def starts_with_s(value):
        if value[0].lower()!='s':
            raise serializers.ValidationError('Must Start with s')
    # title =serializers.CharField(read_only=True)
    title =serializers.CharField(validators=[starts_with_s])
    class Meta:
        model=Article
        fields=['id','title','author','email','date']
        # read_only_fields=['title']
        # extra_kwargs = {'title':{'read_only':True}}

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
