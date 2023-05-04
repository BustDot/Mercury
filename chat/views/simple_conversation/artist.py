import json


def artist(relic_id):
    with open('chat/data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    for museum, relics in json_data.items():
        for relic in relics:
            if relic["id"] == relic_id:
                res = ""
                if relic["artist"] != "" and relic["artist"].lower() != "unknown":
                    res = f"这个文物是由{relic['artist']}创作的"
                else:
                    res = "抱歉，这个文物的作者目前为止还是个迷。"

                return {
                    "relic_id": relic_id,
                    "data": res,
                }
