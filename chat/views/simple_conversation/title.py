import json


def title(relic_id):
    with open('chat/data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    for museum, relics in json_data.items():
        for relic in relics:
            if relic["id"] == relic_id:
                res = ""
                if relic["title"] != "" and relic["title"].lower() != "unknown":
                    res = f"这件文物的名称是{relic['title']}。"
                else:
                    res = "抱歉，无法根据该信息找到文物。"

                return {
                    "relic_id": relic_id,
                    "data": res,
                }
