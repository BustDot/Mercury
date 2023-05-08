import allure
from django.test import TestCase


class TestPostConversation(TestCase):
    @allure.description("test post conversation happy path")
    @allure.severity("P0")
    def test_post_conversation_happy_path_01(self):
        data = {
            "message": "请介绍一下Xu, Beihong",
            "userId": 1
        }
        response = self.client.post("/api/conversation/", data=data)
        self.assertEqual(response.status_code, 200)
