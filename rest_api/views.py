from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_api import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of api view features"""
        my_apiview = [
          'Uses HTTP request as function(get, post, put, delete)',
          'Similar to Django view',
          'Gives you the most control over your app logic',
          'Is mapped manually to URLs',
          ] 
          
        return Response({'message': 'Hallo!', 'my_apiview': my_apiview})

    def post(self, request):
      """Create hello message with name"""
      serializer = self.serializer_class(data=request.data)

      if serializer.is_valid():
        name = serializer.validated_data.get('name')
        message = f'Hallo {name}'
        return Response({'message': message})
      else:
        return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
          )

    def put(self, request, pk=None):
      """Handle updating object"""
      return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
      """Handle partial updating an object"""
      return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
      """Delete object"""
      return Response({'method': 'DELETE'})




