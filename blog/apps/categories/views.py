from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from .models import Category

class CategoryViewSet(GenericAPIView):
    authentication_classes = []
    queryset = Category.objects.all()
    # serializer_class =
    # pagination_class =
    # filter_backends =
    # lookup_field =
    # lookup_url_kwarg =

    def get(self, request):
        categories = Category.objects.all()

    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()

    def get_serializer_class(self):
        """获取序列化器类"""
        pass

    def get_serializer(self, *args, **kwargs):
        """获取序列化器对象"""
        pass
