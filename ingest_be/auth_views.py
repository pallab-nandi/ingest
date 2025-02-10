from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Register View
# POST /register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            user_data = UserSerializer(user, context=self.get_serializer_context()).data
            user_data.pop('password', None)

            return Response({
                "user": user_data,
                "message": "User Created Successfully!",
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                "error": str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
    

# Login View
# POST /login
class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "user": UserSerializer(user).data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": "Invalid Credentials",
                }, status=status.HTTP_401_UNAUTHORIZED)
            
        except Exception as e:
            return Response({
                "error": str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
        

# Logout View
# POST /logout
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({
                "message": "User Logged Out Successfully!"
            }, status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            return Response({
                "error": "Invalid Token",
            }, status=status.HTTP_400_BAD_REQUEST)