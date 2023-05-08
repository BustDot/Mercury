import json


def description(relic_id):
    with open('chat/data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    for museum, relics in json_data.items():
        for relic in relics:
            if relic["id"] == relic_id:
                res = ""
                if relic["description"] != "" and relic["description"].lower() != "unknown":
                    res = f"这个文物的简介为：{relic['description']}"
                else:
                    res = "抱歉，这个文物的简介未被填写"

                return {
                    "relic_id": relic_id,
                    "data": res,
                }
