# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response  # return dict or a list
from rest_framework import status  # statuses, GET, POST, etc.
from profiles_api import serializers
from rest_framework import viewsets


class Hello(APIView):
    """APIView Test"""
    # <-- 'format' is needed to create a suffix for the end of the endpoint
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features (or specific object)"""
        an_apiview = [
            'Uses HTTPS methods as function (get, post, patch, put, delete).',
            'Is similar to a traidtional Django View.',
            'Gives you the most control over your application logic.',
            'Is mapped manually to URLs.'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with out name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Welcome {name}!"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # to update the WHOLE objects
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deleting the whole object"""
        return Response({'method': 'DELETE'})


class HelloViewSets(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message, just like GET request in APIView"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'viewset': a_viewset})

    def create(self, request):
        """Create a new hellow message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Welcome {name}!"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve a specific object from database"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_method": "PATCH"})
    
    def destroy(self, request, pk=None):
        """Handle deleting an object"""
        return Response({"http_method": "DELETE"})