# -*-   coding:utf-8-*-   utf-8�� �ۼ��ϰڴ�.

from django.urls import path
from . import views

urlpatterns = [
  path('',views.index, name = "index"), #views.py 파일에서 index 함수를 찾아라.
  path('createTodo',views.createTodo,name = "createTodo"),#index.html에서 온 createTodo. index.html의 form 태그 action, vies.py에 가서 createTodo 함수를 만들어라.
  path('deleteTodo',views.deleteTodo, name = "deleteTodo")
]
