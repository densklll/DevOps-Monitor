from rest_framework import generics, permissions
from .models import Pipeline, Build, Notification, CISystemIntegration
from .serializers import (
    PipelineSerializer, 
    BuildSerializer, 
    NotificationSerializer, 
    CISystemIntegrationSerializer
)

# Эндпоинты для Pipeline
class PipelineListCreateView(generics.ListCreateAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer
    permission_classes = [permissions.IsAuthenticated]

class PipelineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer
    permission_classes = [permissions.IsAuthenticated]

# Эндпоинты для Build
class BuildListCreateView(generics.ListCreateAPIView):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer
    permission_classes = [permissions.IsAuthenticated]

class BuildDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer
    permission_classes = [permissions.IsAuthenticated]

# Эндпоинты для Notification
class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

# Эндпоинты для CISystemIntegration
class IntegrationListCreateView(generics.ListCreateAPIView):
    queryset = CISystemIntegration.objects.all()
    serializer_class = CISystemIntegrationSerializer
    permission_classes = [permissions.IsAuthenticated]

class IntegrationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CISystemIntegration.objects.all()
    serializer_class = CISystemIntegrationSerializer
    permission_classes = [permissions.IsAuthenticated] 
# 2022-01-12: Adjust K8s CPU requests for backend (staging)

# 2022-01-27: Mark Locust hatch rate on laptop (local dev)

# 2022-02-16: Sketch serializer null owner edge case (staging)
