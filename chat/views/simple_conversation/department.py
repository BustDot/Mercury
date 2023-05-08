import json


def department(relic_id):
    with open('chat/data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    for museum, relics in json_data.items():
        for relic in relics:
            if relic["id"] == relic_id:
                res = ""
                if relic["department"] != "" and relic["department"].lower() != "unknown":
                    res = f"这个文物隶属{relic['department']}部门"
                else:
                    res = "抱歉，这个文物的部门目前为止还是未知。"

                return {
                    "relic_id": relic_id,
                    "data": res,
                }
