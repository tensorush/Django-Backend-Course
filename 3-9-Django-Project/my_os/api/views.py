from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Category, System
from .serializers  import CategorySerializer, SystemSerializer


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = Category()
            category.name = serializer.validated_data['name']
            category.save()
            return Response({'status': 'OK', 'id': category.id})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = None
        try:
            category = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class SystemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = System.objects.all()
        serializer = SystemSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SystemSerializer(data=request.data)
        if serializer.is_valid():
            system = System()
            system.name = serializer.validated_data['name']
            system.logo = serializer.validated_data['logo']
            system.save()
            if 'categories' in request.data:
                categories_list = request.data['categories']
                for category_id in categories_list:
                    try:
                        system.categories.add(Category.objects.get(id=category_id))
                    except:
                        pass
            return Response({'status': 'OK', 'id': system.id})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = System.objects.all()

        system = None
        try:
            system = get_object_or_404(queryset, pk=pk)
        except:
            pass

        if 'categories' in request.data:
            categories_list = request.data['categories']
            system.categories.clear()
            for category_id in categories_list:
                try:
                    system.categories.add(Category.objects.get(id=category_id))
                except:
                    pass
        return Response({'status': 'OK'})

    def retrieve(self, request, pk=None):
        queryset = System.objects.all()
        system = None
        try:
            system = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = SystemSerializer(system)
        return Response(serializer.data)
