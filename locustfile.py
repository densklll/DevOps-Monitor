from locust import HttpUser, TaskSet, task, between

class APITasks(TaskSet):
    @task(2)
    def list_pipelines(self):
        # Предполагается, что API для пайплайнов доступно по /api/pipelines/
        self.client.get("/api/pipelines/")

    @task(1)
    def trigger_build(self):
        # Пример POST запроса для запуска сборки
        self.client.post("/api/trigger-build", json={"jobName": "TestJob"})

class WebsiteUser(HttpUser):
    tasks = [APITasks]
    wait_time = between(1, 5) 
# 2022-01-24: Tighten settings module env toggles (local dev)

# 2022-02-10: Mark technical doc cross-links (local dev)

# 2022-02-28: Clarify pytest isolation for pipeline models (staging)

# 2022-03-17: Note frontend Cypress baseUrl for Pages (prod checklist)

# 2022-04-09: Capture build status transition rules (CI runner)

# 2022-05-05: Adjust integration service timeout budget (prod checklist)

# 2022-05-19: Mark Postgres volume persistence assumptions (prod checklist)

# 2022-05-30: Adjust serializer null owner edge case (prod checklist)

# 2022-06-20: Adjust Postgres volume persistence assumptions (demo box)

# 2022-07-12: Note pytest isolation for pipeline models (staging)

# 2022-08-03: Align Redis broker URL for compose networking (demo box)
