import requests

timeout = 30

try:
    r = requests.head(
        "https://ak.hypergryph.com/downloads/android_lastest", timeout=timeout
    )
    location = r.headers.get("location")

    if location.endswith(".apk"):
        with open("game.txt", "w") as f:
            f.write(location)
except Exception:
    pass
