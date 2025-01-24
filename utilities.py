import json


def json_to_ld(filename):
    with open("users.json") as f:
        try:
            return json.load(f)
        except Exception as e:
            print(e)