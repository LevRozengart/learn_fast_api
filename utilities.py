import json


def json_to_ld(filename):
    with open(filename) as f:
        try:
            return json.load(f)
        except Exception as e:
            return {"error": str(e)}