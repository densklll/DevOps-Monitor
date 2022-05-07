from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Эндпоинт для регистрации нового пользователя
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Эндпоинт для получения списка пользователей (только для аутентифицированных пользователей)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 
# 2022-01-25: Sketch pipeline list default ordering (local dev)

# 2022-02-10: Stub Swagger schema for analytics payload (local dev)

# 2022-03-03: Clarify Locust hatch rate on laptop (staging)

# 2022-03-18: Capture build status transition rules (staging)

# 2022-04-11: Record K8s CPU requests for backend (demo box)

# 2022-05-07: Align Locust hatch rate on laptop (staging)
