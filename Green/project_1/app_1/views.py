from django.shortcuts import render
from .models import Batsman
from .serializers import*
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import*

# Create your views here.
class Batsmanlist(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Batsman.objects.all()
    serializer_class=batsmanserializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    # def get(self,request,**kwargs):
    #     return self.retrieve(request,**kwargs)
    # def put(self,request,**kwargs):
    #     return self.update(request,**kwargs)
    # def delete(self,request,**kwargs):
    #     return self.destroy(request,**kwargs)


class Batsmanchecklist(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Batsman.objects.all()
    serializer_class=batsmanserializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)

