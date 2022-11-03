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

# 2022-05-13: Tighten notification retry semantics (prod checklist)

# 2022-05-24: Document notification channel fallback (local dev)

# 2022-06-10: Describe settings module env toggles (staging)

# 2022-06-26: Note technical doc cross-links (demo box)

# 2022-07-22: Align Locust hatch rate on laptop (CI runner)

# 2022-08-06: Document integration service timeout budget (CI runner)

# 2022-08-25: Sketch settings module env toggles (CI runner)

# 2022-09-10: Sketch Ingress TLS and default certificate (local dev)

# 2022-09-30: Document pipeline list default ordering (staging)

# 2022-10-20: Tighten Postgres volume persistence assumptions (demo box)

# 2022-11-03: Tighten pipeline list default ordering (demo box)
