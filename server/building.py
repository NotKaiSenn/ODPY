from flask import request

from utils import read_json, write_json
from core.function.update import updateData
from constants import BUILDING_JSON_PATH, USER_JSON_PATH, BUILDING_TABLE_URL


def updateBuildingCharInstIdList(building_data):
    for i in building_data["chars"]:
        building_data["chars"][i]["roomSlotId"] = ""
        building_data["chars"][i]["index"] = -1
    for i in building_data["roomSlots"]:
        for j, k in enumerate(building_data["roomSlots"][i]["charInstIds"]):
            if k == -1:
                continue
            k = str(k)
            building_data["chars"][k]["roomSlotId"] = i
            building_data["chars"][k]["index"] = j


def buildingSync():
    building_data = read_json(BUILDING_JSON_PATH)
    user_data = read_json(USER_JSON_PATH)
    chars = {
        i: {
            "charId": user_data["user"]["troop"]["chars"][i]["charId"],
            "lastApAddTime": 1695000000,
            "ap": 8640000,
            "roomSlotId": "",
            "index": -1,
            "changeScale": 0,
            "bubble": {
                "normal": {
                    "add": -1,
                    "ts": 0
                },
                "assist": {
                    "add": -1,
                    "ts": 0
                }
            },
            "workTime": 0
        } for i in user_data["user"]["troop"]["chars"]
    }
    building_data["chars"] = chars
    updateBuildingCharInstIdList(building_data)
    building_table = updateData(BUILDING_TABLE_URL)
    furniture = {
        i: {
            "count": 9999,
            "inUse": 0
        } for i in building_table["customData"]["furnitures"]
    }
    building_data["furniture"] = furniture
    write_json(building_data, BUILDING_JSON_PATH)
    data = {
        "playerDataDelta": {
            "modified": {
                "building": building_data
            },
            "deleted": {}
        }
    }
    return data


def building_getRecentVisitors():
    return {"visitors": []}


def building_getInfoShareVisitorsNum():
    return {"num": 0}


def building_changeDiySolution():
    request_data = request.get_json()
    roomSlotId = request_data["roomSlotId"]
    diySolution = request_data["solution"]

    building_data = read_json(BUILDING_JSON_PATH)
    building_data["rooms"]["DORMITORY"][roomSlotId]["diySolution"] = diySolution
    write_json(building_data, BUILDING_JSON_PATH)
    data = {
        "playerDataDelta": {
            "modified": {
                "building": building_data
            },
            "deleted": {}
        }
    }
    return data


def building_assignChar():
    request_data = request.get_json()
    roomSlotId = request_data["roomSlotId"]
    charInstIdList = request_data["charInstIdList"]

    building_data = read_json(BUILDING_JSON_PATH)
    for i in charInstIdList:
        if i == -1:
            continue
        i = str(i)
        if building_data["chars"][i]["index"] != -1:
            old_roomSlotId = building_data["chars"][i]["roomSlotId"]
            old_index = building_data["chars"][i]["index"]
            building_data["roomSlots"][old_roomSlotId]["charInstIds"][old_index] = -1
    building_data["roomSlots"][roomSlotId]["charInstIds"] = charInstIdList
    updateBuildingCharInstIdList(building_data)
    write_json(building_data, BUILDING_JSON_PATH)
    data = {
        "playerDataDelta": {
            "modified": {
                "building": building_data
            },
            "deleted": {}
        }
    }
    return data


def building_setBuildingAssist():
    request_data = request.get_json()

    building_data = read_json(BUILDING_JSON_PATH)
    building_data["assist"][request_data["type"]] = request_data["charInstId"]
    write_json(building_data, BUILDING_JSON_PATH)
    data = {
        "playerDataDelta": {
            "modified": {
                "building": building_data
            },
            "deleted": {}
        }
    }
    return data


def building_getAssistReport():
    return {
        "reports": [
        ],
        "playerDataDelta": {
            "modified": {},
            "deleted": {}
        }
    }
