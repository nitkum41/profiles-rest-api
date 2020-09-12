from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


# Create your views here.
class HelloApiView(APIView):
    """ Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return list of APIView features"""
        #
        an_apiview = ['uses HTTP methods (get, post ,put, patch ,delete) as functions',
                      'is similar to traditional django view',
                      'gives control over app logic',
                      'is mapped manually to URLs']
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        """create a hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """handle partial update of  an object with parameters provided only"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        "returns a hello message"
        a_viewset = ['uses actions list,create,retrieve,update,partial_update,destroy',
                    'automatically maps to urls using routers',
                    'more functionality with less code']
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """create new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """ handle getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """ handle updating an object """
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """ handle partial updating an object """
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """delete an object"""
        return Response({'http_method':'DELETE'})
