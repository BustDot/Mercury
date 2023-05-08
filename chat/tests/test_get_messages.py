import logging

import allure
from django.test import TestCase


class TestGetMessages(TestCase):

    def setUp(self) -> None:
        data = {
            "relic_id": "O23712",
            "question_type": "artist",
            "userId": "1"
        }
        self.client.post("/api/simple_conversation/", data=data)

    @allure.description("test get messages happy path")
    @allure.severity("P0")
    def test_get_messages_happy_path_01(self):
        response = self.client.get("/api/chat/messages/", data={"userId": "1"})
        logging.info(msg=response.status_code)
        self.assertEqual(response.status_code, 200)
