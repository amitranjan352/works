
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet,Register
from.serializers import RegisterSerializer, LoginSerializer,SnippetSerializer
from rest_framework.views import APIView
from django.http import Http404




# @api_view(['GET', 'POST'])
# def amit(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Register(generics.ListCreateAPIView):
#     queryset = Register.objects.all()
#     serializer_class = RegisterSerializer


class Login(APIView):

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username and password:
            user_obj = Register.objects.filter(username=username, password=password).exists()
            if user_obj:
                user = LoginSerializer(user_obj)
                print(user_obj)
                data_list = {}
                data_list.update(user.data)
                return Response({"message": "Login Successfully", "data":data_list, "code": 200})
            else:
                return Response({"message": "unablE", "code": 500, 'data': {}})
        else:
            message = "Invalid login details."
            return Response({"message": message, "code": 500, 'data': {}})
               
         
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






        
