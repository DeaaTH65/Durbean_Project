from rest_framework import viewsets, status
from rest_framework.response import Response
from accounts.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/users',
        'GET /api/login',
        'GET /api/register',
    ]
    return Response(routes)



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        User = get_user_model()
        try:
            user = User.objects.get(phone=phone)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'detail': 'User with provided phone does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'detail': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
