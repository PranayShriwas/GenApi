from rest_framework import serializers
from .models import *

class AuthorSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"
        
class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"