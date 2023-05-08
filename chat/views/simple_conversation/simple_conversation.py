from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chat.models import Conversation, Message
from chat.views.simple_conversation.artist import artist
from chat.views.simple_conversation.role import role
from chat.views.simple_conversation.description import description

question_types = {
    'artist': artist,
    'role': role,
    'description': description,
}

messages = {
    'artist': "是谁创造了这个文物？",
    'role': "这个文物是什么类型？",
    'description': "简单介绍一下这个文物",
}


@api_view(['POST'])
def simple_conversation(request):
    relic_id = request.data.get('relic_id')
    question_type = request.data.get('question_type')
    user_id = request.data.get('userId')
    if question_type in question_types:
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
            message=messages[question_type]
        )
        message_obj.save()
        func = question_types[question_type]
        data = func(relic_id)
        ai_message_obj = Message(
            conversation_id=conversation_obj.id,
            message=data.get("data"),
            is_bot=True
        )
        ai_message_obj.save()
        response = {'data': data, 'result': 'success'}
        return Response(data=response)
    else:
        response = {'result': 'error', "message": 'invalid question_type.'}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
