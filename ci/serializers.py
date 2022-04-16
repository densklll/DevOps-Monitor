from rest_framework import serializers
from .models import Pipeline, Build, Notification, CISystemIntegration

class PipelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipeline
        fields = '__all__'

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class CISystemIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CISystemIntegration
        fields = '__all__' 
# 2022-01-17: Tighten settings module env toggles (staging)

# 2022-01-30: Capture Redis broker URL for compose networking (prod checklist)

# 2022-02-18: Adjust notification channel fallback (demo box)

# 2022-03-09: Describe serializer null owner edge case (staging)

# 2022-03-28: Sketch serializer null owner edge case (prod checklist)

# 2022-04-16: Mark settings module env toggles (staging)
