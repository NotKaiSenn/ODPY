from flask import request
from constants import USER_JSON_PATH
from utils import read_json, write_json

def backgroundSetBackground():

    data = request.data
    request_data = request.get_json()

    bgID = request_data["bgID"]
    data = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "background": {
                    "selected": bgID
                }
            }
        }
    }

    saved_data = read_json(USER_JSON_PATH)
    saved_data["user"]["background"]["selected"] = bgID
    write_json(saved_data, USER_JSON_PATH)

    return data


def homeThemeChange():
    request_data = request.get_json()

    themeId = request_data["themeId"]

    data = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "homeTheme": {
                    "selected": themeId
                }
            }
        }
    }

    saved_data = read_json(USER_JSON_PATH)
    saved_data["user"]["homeTheme"]["selected"] = themeId
    write_json(saved_data, USER_JSON_PATH)

    return data
