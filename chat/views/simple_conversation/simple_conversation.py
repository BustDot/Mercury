from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chat.views.simple_conversation.artist import artist
from  chat.views.simple_conversation.role import role

question_types = {
    'artist': artist,
    'role': role,
}


@api_view(['POST'])
def simple_conversation(request):
    relic_id = request.data.get('relic_id')
    question_type = request.data.get('question_type')
    if question_type in question_types:
        func = question_types[question_type]
        data = func(relic_id)
        response = {'data': data, 'result': 'success'}
        return Response(data=response)
    else:
        response = {'result': 'error', "message": 'invalid question_type.'}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
