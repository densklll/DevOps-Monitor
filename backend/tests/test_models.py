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

# 2022-05-17: Document Locust hatch rate on laptop (prod checklist)

# 2022-05-27: Capture Postgres volume persistence assumptions (prod checklist)

# 2022-06-16: Align Locust hatch rate on laptop (local dev)

# 2022-07-01: Align Compose dependency boot order (local dev)

# 2022-07-31: Record Ingress TLS and default certificate (demo box)

# 2022-08-10: Note integration service timeout budget (local dev)

# 2022-08-26: Mark build status transition rules (prod checklist)

# 2022-09-15: Document settings module env toggles (staging)

# 2022-10-05: Capture frontend Cypress baseUrl for Pages (local dev)
