from locust import task, FastHttpUser, between
import random

fruits = ["Apple", "Apricot", "Avocado", "Banana", "Cherry", "Coconut", "Dates", "Grapefruit", "Guava",
          "Lemon", "Lychee", "Mandarin", "Mango", "Pineapple", "Watermelon"]


class DemoUser(FastHttpUser):
    host = "https://www.bing.com"
    wait_time = between(1, 2)

    @task
    def index(self):
        self.client.get("/search?q={keyword}".format(keyword=random.choice(fruits)))
