from django.test import TestCase


class TestGetConversations(TestCase):
    def test_get_conversation_happy_path_01(self):
        response = self.client.get("/api/chat/conversations/", data={"userId": "1"})
        self.assertEqual(response.status_code, 200)
