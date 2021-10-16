from django.shortcuts import render
from .models import Home
from .serializer import HomeSerialzer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.


class HomeAPIVieew(APIView):

    def get(self, request, format=None):
        home_list = Home.objects.all()
        home_serializer = HomeSerialzer(home_list, many=True)
        return Response(home_serializer.data)


class HomeListAPIView(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerialzer

    def get_queryset(self):
        name = self.kwargs['name']
        return Home.objects.filter(name=name)


class HomeCreateAPIView(CreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerialzer


class HomeDetailsAPIView(RetrieveAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerialzer


class HomeUpdateAPIView(UpdateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerialzer


class HomeDeleteAPIView(DestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerialzer