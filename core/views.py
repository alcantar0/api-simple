from django.shortcuts import render

# Create your views here.
from users.models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import CustomUserSerializer
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def get_token(self, request):
        try:
            id = CustomUser.objects.get(email=request.data['email'], password=request.data['password']).id
        except ObjectDoesNotExist:
            return Response({"erro": "email ou senha incorretos"})

        token = Token.objects.get(user_id=id)
        return Response({"token": str(token)})
