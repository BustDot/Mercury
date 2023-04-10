import os

import requests
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from chat.models import Conversation, Message

load_dotenv()

MURA_URL = "https://api.usemeru.com/refine/v4"

MODEL = {
    "model_id": "context-text-davinci-003",
    "inputs": {
        "file_id": "83f53a84-b289-46cf-a8ae-7d178b9d9ebc",
        "prompt": "",
        "temperature": 0.5,
        "max_tokens": 512
    }
}


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def conversation(request):
    api_key = get_api_key()
    if api_key is None:
        return Response(
            {
                'error': 'The administrator has not set the API key'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    model = MODEL
    message = request.data.get('message')
    conversation_id = request.data.get('conversationId')

    if conversation_id:
        # get the conversation
        conversation_obj = Conversation.objects.get(id=conversation_id)
    else:
        # create a new conversation
        conversation_obj = Conversation(user=request.user)
        conversation_obj.save()
    # insert a new message
    message_obj = Message(
        conversation_id=conversation_obj.id,
        message=message
    )
    message_obj.save()

    try:
        model["inputs"]["prompt"] = message
        headers = {
            "x-api-key": f"{api_key}",
            "Content-Type": "application/json"
        }
        res = requests.post(f"{MURA_URL}/predict", headers=headers, json=model)
        if not res.ok:
            raise Exception(f'Failed to fetch: {res.status_code} {res.reason}')

        data = res.json()
        if data.get("err_code") != 0:
            raise Exception(f'Something went wrong: {data.get("err_msg")}')
        response = {
            "data": data.get("outputs").get("choices")[0].get("text"),
            "conversation_id": conversation_obj.id
        }
        ai_message_obj = Message(
            conversation_id=conversation_obj.id,
            message=response.get("data"),
            is_bot=True
        )
        ai_message_obj.save()
    except Exception as e:
        print(e)
        return Response(
            {
                'error': e
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(response, status=status.HTTP_200_OK)


def get_api_key():
    api_key = os.getenv("API_KEY")
    if api_key:
        return api_key
    return None

