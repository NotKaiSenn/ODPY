import json

try:
    with open("data/excel/activity_table.json", encoding="utf-8") as f:
        activity_table = json.load(f)

    activity_start_time_list = []

    for i in activity_table["basicInfo"]:
        if i.endswith("side") or i.endswith("sre"):
            startTime = activity_table["basicInfo"][i]["startTime"]
            activity_start_time_list.append(startTime)

    max_activity_start_time = max(activity_start_time_list)

    with open("config/config.json") as f:
        config = json.load(f)

    config["userConfig"]["activityStartTs"] = max_activity_start_time - \
        (7*24*60*60)

    with open("config/config.json", "w") as f:
        json.dump(config, f, indent=4)
except Exception:
    pass
