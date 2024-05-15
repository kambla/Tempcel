
from locust import HttpUser, TaskSet, task, between
import random

class UserBehavior(TaskSet):
   @task(1)
   def convert_to_celsius(self):
       fahrenheit = round(random.uniform(0, 200), 1)
       self.client.get(f"/fahrenheit_to_celsius/{fahrenheit}")

class WebsiteUser(HttpUser):
    tasks = {UserBehavior}
    wait_time = between(1, 3)
