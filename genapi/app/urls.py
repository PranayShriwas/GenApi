from django.contrib import admin
from django.urls import path,include
from rest_framework import generics
from .views import Authorcreate,Authordelete,AuthorList,AuthorReteriveApi,AuthorUpdate,PostGetApi,PostcreateApi,PostdelteApi,PostreteriveApi,PostUpdateApi
urlpatterns = [
    path('',AuthorList.as_view()),
    path('authorcreate/',Authorcreate.as_view()),
    path('authordelete/<int:pk>',Authordelete.as_view()),
    path('authorupdate/<int:pk>',AuthorUpdate.as_view()),
    path('authorreterive/<int:pk>',AuthorReteriveApi.as_view()),
    path('postapi/',PostGetApi.as_view()),
    path('postcreate/',PostcreateApi.as_view()),
    path('postdelete/<int:pk>',PostdelteApi.as_view()),
    path('postupdate/<int:pk>',PostUpdateApi.as_view()),
    path('postreterive/<int:pk>',PostreteriveApi.as_view())
    
    
]
