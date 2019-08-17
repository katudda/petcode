from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions
from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from petcode.pets.models import PetType, Size, Gender, Pet, CategoryStatus, Category
from petcode.pets.serializers import UserSerializer, PetTypeSerializer, SizeSerializer, GenderSerializer, PetSerializer, CategorySerializer, CategoryStatusSerializer
from django.views.decorators.csrf import csrf_exempt

############################################################################
# Permissoes customizadas
############################################################################
class PublicRetrieveAndListOnly(permissions.IsAuthenticated):
    """
    Custom permission to only allow list and retrieve without authorization
    """
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        else:
            return bool(request.user and request.user.is_authenticated)


class PublicCreateOnly(permissions.IsAuthenticated):
    """
    Custom permission to only allow create without authorization
    """
    def has_permission(self, request, view):
        if view.action in ['create',]:
            return True
        else:
            return bool(request.user and request.user.is_authenticated)

############################################################################
# FIM Permissoes customizadas
############################################################################



class PetTypeViewSet(viewsets.ModelViewSet):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryStatusViewSet(viewsets.ModelViewSet):
    queryset = CategoryStatus.objects.all()
    serializer_class = CategoryStatusSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [PublicRetrieveAndListOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category', 'user', 'name', 'gender', 'size', 'state', 'city', 'published_date']

    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [PublicCreateOnly]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        response = {}
        response['username'] = username
        response['token'] = token.key
        return Response(response,
                        status=HTTP_200_OK)
