from rest_framework import generics
from rest_framework.authentication import TokenAuthentication,SessionAuthentication

from .models import Author
from .serializers import AuthorSerializer

class AuthorRegisterView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]