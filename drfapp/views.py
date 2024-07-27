from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team
from .serializers import UserSerializer, TeamSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def team(request):
    if request.method == 'GET':
        obj = Team.objects.all()
        serializer = TeamSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PUT':
        obj = Team.objects.get(id=request.data['id'])
        serializer = TeamSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PATCH':
        obj = Team.objects.get(id=request.data['id'])
        serializer = TeamSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        obj = Team.objects.get(id=request.data['id'])
        obj.delete()
        return Response("deleted")
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def user(request):
    if request.method == 'GET':
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PUT':
        obj = User.objects.get(id=request.data['id'])
        serializer = UserSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PATCH':
        obj = User.objects.get(id=request.data['id'])
        serializer = UserSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        obj = User.objects.get(id=request.data['id'])
        obj.delete()
        return Response("deleted")
    
from rest_framework.views import APIView

class UserList(APIView):
    def get(self, request):
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response("serializer.data")

    def post(self, request):
        data = request.data 
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__icontains=search)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    