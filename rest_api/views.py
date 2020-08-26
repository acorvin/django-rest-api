from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test api view"""
    def get(self, request, format=None):
        """Return a list of api view features"""
        my_apiview = [
          'Uses HTTP request as function(get, post, put, delete)',
          'Similar to Django view',
          'Gives you the most control over your app logic',
          'Is mapped manually to URLs',
          ] 
          
        return Response({'message': 'Hello!', 'my_apiview': my_apiview})
