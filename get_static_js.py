import json

with open("config/config.json") as f:
    config = json.load(f)
server = config["server"]
HOST = server["host"]
PORT = server["port"]
MODE = server["mode"]
ACTIVITY_START_TS = config["userConfig"]["activityStartTs"]

with open("_.js", encoding="utf-8") as f:
    s = f.read()

s = s.replace(
    "@@@DOCTORATE_HOST@@@", HOST, 1
).replace(
    "@@@DOCTORATE_PORT@@@", str(PORT), 1
).replace(
    "@@@DOCTORATE_ACTIVITY_START_TS@@@", str(ACTIVITY_START_TS), 1
)

with open("_.static.js", "w", encoding="utf-8") as f:
    f.write(s)
