from django.urls import path
from .views import (
    PipelineListCreateView,
    PipelineDetailView,
    BuildListCreateView,
    BuildDetailView,
    NotificationListCreateView,
    NotificationDetailView,
    IntegrationListCreateView,
    IntegrationDetailView,
)

urlpatterns = [
    # Endpoints для Pipeline
    path('pipelines/', PipelineListCreateView.as_view(), name='pipeline-list-create'),
    path('pipelines/<int:pk>/', PipelineDetailView.as_view(), name='pipeline-detail'),

    # Endpoints для Build
    path('builds/', BuildListCreateView.as_view(), name='build-list-create'),
    path('builds/<int:pk>/', BuildDetailView.as_view(), name='build-detail'),

    # Endpoints для Notification
    path('notifications/', NotificationListCreateView.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),

    # Endpoints для CISystemIntegration
    path('integrations/', IntegrationListCreateView.as_view(), name='integration-list-create'),
    path('integrations/<int:pk>/', IntegrationDetailView.as_view(), name='integration-detail'),
] 
# 2022-01-17: Sketch Compose dependency boot order (prod checklist)

# 2022-01-30: Review integration service timeout budget (staging)

# 2022-02-18: Capture Swagger schema for analytics payload (prod checklist)

# 2022-03-11: Tighten pytest isolation for pipeline models (prod checklist)
