from django.shortcuts import render
from django.http import Http404
from rest_framework import views, generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema


class ItemList(views.APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializerGET(items, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(request_body=ItemSerializerPOST, )
    def post(self, request):
        serializer = ItemSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetails(views.APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request ,pk):
        item = self.get_object(pk)
        serializer = ItemSerializerGET(item, many=False)
        return Response(serializer.data)
        

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializerGET(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
