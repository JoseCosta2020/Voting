from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'polls'

urlpatterns = [
    path('first', views.index, name='viewIndex'),
    path('Godo', views.Goods, name='viewGoods'),
    path('iGodo2', views.Goods2, name='viewsGoods2'),    
    path('testar', views.testarm, name="viewTestar"),
    path('<int:question_id>/', views.detail, name='viewDetail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]