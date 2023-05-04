from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

with open('chat/static/data1.json', 'r') as file:
    json_data = json.load(file)


def artist(relic_id):
    for museum in json_data:
        for relic in museum:
            if relic["id"] == relic_id:
                res = ""
                if relic["artist"] != "" or relic["artist"].lower() != "unknown":
                    res = f"这个文物是由{relic['artist']}创作的"
                else:
                    res = "抱歉，这个文物的作者目前为止还是个迷。"

                return {
                    "relic_id": relic_id,
                    "data": res,
                    "result": "success"
                }


question_types = {
    'artist': artist,
}


@api_view(['POST'])
def simple_conversation(request):
    data = {}
    # try:
    relic_id = request.data.get('relic_id')
    question_type = request.data.get('question_type')
    if question_type in question_types:
        func = question_types["question_type"]
        print(func)
        data = func(relic_id)
    response = {'data': data, 'result': 'success'}
    return Response(data=response)
    # except:
    #     response = {'result': 'error'}
    #     return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
