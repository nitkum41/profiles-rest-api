from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """ Test APIView"""

    def get(self, request, format=None):
        """return list of APIView features"""
        #
        an_apiview = ['uses HTTP methods (get, post ,put, patch ,delete) as functions',
                      'is similar to traditional django view',
                      'gives control over app logic',
                      'is mapped manually to URLs']
        return Response({'message':'hello','an_apiview':an_apiview})
