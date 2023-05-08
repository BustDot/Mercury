import allure
from django.test import TestCase


class TestPostSimpleConversation(TestCase):
    @allure.description("test post simple conversation happy path")
    @allure.severity("P0")
    def test_post_simple_conversation_happy_path_01(self):
        data = {
            "relic_id": "O23712",
            "question_type": "artist",
            "userId": "1"
        }
        response = self.client.post("/api/simple_conversation/", data=data)
        self.assertEqual(response.status_code, 200)
