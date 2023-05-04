import json


def artist(relic_id):
    with open('../../static/data.json', 'r') as file:
        data = json.load(file)
        for museum in data:
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
