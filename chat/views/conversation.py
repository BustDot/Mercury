import os

import requests
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat.models import Conversation, Message

load_dotenv()

MURA_URL = "https://api.usemeru.com/refine/v4"

MODEL = {
    "model_id": "context-text-davinci-003",
    "inputs": {
        "file_id": "",
        "prompt": "",
        "temperature": 0.5,
        "max_tokens": 512
    }
}


@api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def conversation(request):
    api_key = get_api_key()
    file_id = get_file_id()
    if api_key is None:
        return Response(
            {
                'error': 'The administrator has not set the API key'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    model = MODEL
    message = request.data.get('message')
    user_id = request.data.get('userId')

    if user_id is None:
        return Response(
            {
                'error': 'Invalid userId'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        if not Conversation.objects.filter(user=user_id).exists():
            # create a new conversation
            conversation_obj = Conversation(user=user_id)
            conversation_obj.save()
    conversation_obj = Conversation.objects.get(user=user_id)
    # insert a new message
    message_obj = Message(
        conversation_id=conversation_obj.id,
        message=message
    )
    message_obj.save()

    try:
        model["inputs"]["prompt"] = "你是mercury,一名研究中国文物的专家。请用中文回答," + message
        model["inputs"]["file_id"] = file_id

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
            "conversation_id": conversation_obj.id,
            "result": "success"
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


def get_file_id():
    file_id = os.getenv("FILE_ID")
    if file_id:
        return file_id
    return None
