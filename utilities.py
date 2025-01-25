import json


def json_to_ld(filename):
    with open(filename) as f:
        try:
            return json.load(f)
        except Exception as e:
            return {"error": str(e)}


def ld_to_json(ld, filename):
    with open(filename, "w") as f:
        try:
            json.dump(ld, f, indent=2)
            return {"success", True}
        except Exception as e:
            return {"erroe": str(e)}

def append_user(lst_of_users: list, username: str, password: str):
    try:
        lst_of_users.append({"username": username, "password": password, "admin": False})
        return lst_of_users
    except Exception as e:
        return {"error": 400}
