from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class = HelloSerializer
    
    def get(self,request, format=None):
        """Returns a list of APIView Features."""

        
        an_apiview = [
            "Uses HTTP methods as function (get,post, patch, put, delete)",
            "It is similar to a atraditional Django View",
            "Gives you the most control over your logic",
            "Is mapped manually to URLs"
        ]
        
        return Response({"message": "Hello!", 'an_appview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name."""

        serializer = HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'method':'put'})

        
    def patch(self, request, pk=None):
        """Patch request, only updates field provided in the request"""

        return Response({'method':'patch'})
            
        
    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method':'delete'})
            
        