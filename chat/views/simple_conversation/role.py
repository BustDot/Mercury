import json


def role(relic_id):
    with open('chat/data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    for museum, relics in json_data.items():
        for relic in relics:
            if relic["id"] == relic_id:
                res = ""
                if relic["role"] != "" and relic["role"].lower() != "unknown":
                    res = f"The role of this cultural relic is {relic['role']}"
                else:
                    res = "Sorry,the role of this culture relic is still unknown."

                return {
                    "relic_id": relic_id,
                    "data": res,
                }
