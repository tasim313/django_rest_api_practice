from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('home_api/<name>', views.HomeListAPIView.as_view(), name='home_api'),
    path('', views.HomeAPIVieew.as_view(), name='home'),
    path('create/', views.HomeCreateAPIView.as_view(), name='create'),
    path('details/<pk>/', views.HomeDetailsAPIView.as_view(), name='details'),
    path('update/<pk>/', views.HomeUpdateAPIView.as_view(), name='update'),
    path('delete/<pk>/', views.HomeDeleteAPIView.as_view(), name='Delete'),

]
