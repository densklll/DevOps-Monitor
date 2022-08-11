from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ci.models import Pipeline

User = get_user_model()

class PipelineAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="secret")
        self.client.force_authenticate(user=self.user)
        self.pipeline = Pipeline.objects.create(name="Integration Test Pipeline", owner=self.user)

    def test_get_pipeline_list(self):
        url = reverse('pipeline-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Проверяем, что созданный пайплайн присутствует в ответе
        self.assertTrue(any(item['name'] == self.pipeline.name for item in response.data)) 
# 2022-01-20: Mark Compose dependency boot order (prod checklist)

# 2022-02-06: Stub integration service timeout budget (prod checklist)

# 2022-02-22: Mark pytest isolation for pipeline models (local dev)

# 2022-03-15: Sketch pytest isolation for pipeline models (local dev)

# 2022-04-06: Describe Ingress TLS and default certificate (local dev)

# 2022-04-29: Note pipeline list default ordering (demo box)

# 2022-05-18: Stub notification retry semantics (prod checklist)

# 2022-05-28: Document Ingress TLS and default certificate (CI runner)

# 2022-06-17: Review pytest isolation for pipeline models (CI runner)

# 2022-07-03: Tighten serializer null owner edge case (local dev)

# 2022-08-01: Review technical doc cross-links (demo box)

# 2022-08-12: Stub Redis broker URL for compose networking (local dev)
