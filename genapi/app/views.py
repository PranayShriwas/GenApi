from django.shortcuts import render
from .serilizer import PostSerilizer,AuthorSerilizer
from .models import *
from rest_framework import generics
# Create your views here.

class AuthorList(generics.ListAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerilizer

class Authorcreate(generics.CreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerilizer
    
class AuthorUpdate(generics.UpdateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerilizer
    
class Authordelete(generics.DestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerilizer
    
class AuthorReteriveApi(generics.RetrieveAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerilizer
    

class PostGetApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerilizer

class PostUpdateApi(generics.UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerilizer
    
class PostcreateApi(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerilizer
    
class PostdelteApi(generics.DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerilizer
    
class PostreteriveApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerilizer
    