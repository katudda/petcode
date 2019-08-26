from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .permissions import PublicCreateOnly
from rest_framework.decorators import action
from django.contrib.auth import authenticate
# from .authentication import authenticate
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [PublicCreateOnly]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        import ipdb ; ipdb.set_trace()
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=HTTP_400_BAD_REQUEST)
        username = User.objects.get(email=email).username
        user = authenticate(username=username, password=password)
        # user = authenticate(self, email=email, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        response = {}
        response['email'] = email
        response['token'] = token.key
        return Response(response,
                        status=HTTP_200_OK)