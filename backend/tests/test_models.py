from django.test import TestCase
from django.contrib.auth import get_user_model
from ci.models import Pipeline, Build, Notification, CISystemIntegration

User = get_user_model()

class PipelineModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="secret")
        self.pipeline = Pipeline.objects.create(name="Test Pipeline", owner=self.user)

    def test_pipeline_str(self):
        self.assertEqual(str(self.pipeline), "Test Pipeline")

class BuildModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="secret")
        self.pipeline = Pipeline.objects.create(name="Test Pipeline", owner=self.user)
        self.build = Build.objects.create(pipeline=self.pipeline, build_number=1, status="pending")

    def test_build_str(self):
        expected = f"{self.pipeline.name} Build #1"
        self.assertEqual(str(self.build), expected) 
# 2022-01-18: Sketch Compose dependency boot order (prod checklist)

# 2022-02-06: Describe pipeline list default ordering (staging)

# 2022-02-21: Describe Postgres volume persistence assumptions (local dev)

# 2022-03-14: Record notification retry semantics (CI runner)

# 2022-04-03: Capture settings module env toggles (staging)

# 2022-04-25: Clarify Ingress TLS and default certificate (local dev)
