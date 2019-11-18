from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated

class TestView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        data = Post.objects.all()
        serializer = PostSerializer(data, many=True)
        
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

        


# def get(request):
#     data = {
#         'name': 'nabil',
#         'id': 'loser'
#     }
#     return JsonResponse(data)
