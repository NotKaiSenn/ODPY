import subprocess
import json
import os
import requests
import shutil
from zipfile import ZipFile

with open("config/config.json") as f:
    config = json.load(f)
res_version = config["version"]["android"]["resVersion"]


if shutil.which("aria2c") is None:
    aria2_url = "https://github.com/aria2/aria2/releases/download/release-1.37.0/aria2-1.37.0-win-64bit-build1.zip"
    r = requests.get(
        "https://api.github.com/repos/aria2/aria2/releases/latest"
    )
    s = r.json()
    for i in s["assets"]:
        if i["name"].startswith("aria2") and i["name"].endswith(".zip") and i["name"].find("win-64bit") != -1:
            aria2_url = i["browser_download_url"]
            break
    aria2_file_name = os.path.basename(aria2_url)
    if not os.path.exists(aria2_file_name):
        print("Download:", aria2_file_name)
        subprocess.run(
            [
                "curl", "-L", "-O", aria2_url
            ]
        )
    print("Use:", aria2_file_name)
    with ZipFile(aria2_file_name) as f:
        aria2_namelist = f.namelist()
        for name in aria2_namelist:
            if name.endswith("aria2c.exe"):
                with open("aria2c.exe", "wb") as fout:
                    fout.write(f.read(name))
                    break


os.makedirs(f"assets/{res_version}/redirect/", exist_ok=True)

subprocess.run(
    [
        "curl", "-L", "-O",
        "--output-dir", f"assets/{res_version}/redirect/",
        f"https://ak.hycdn.cn/assetbundle/official/Android/assets/{res_version}/hot_update_list.json"
    ]
)


with open(f"assets/{res_version}/redirect/hot_update_list.json") as f:
    hot_update_list = json.load(f)

url_list = []

for i in hot_update_list["packInfos"]:
    filename = i["name"].replace(
        '/', '_'
    ).replace(
        '#', "__"
    )+".dat"
    url_list.append(
        f"https://ak.hycdn.cn/assetbundle/official/Android/assets/{res_version}/{filename}"
    )


for i in hot_update_list["abInfos"]:
    filename = os.path.splitext(
        i["name"].replace(
            '/', '_'
        ).replace(
            '#', "__"
        )
    )[0]+".dat"
    url_list.append(
        f"https://ak.hycdn.cn/assetbundle/official/Android/assets/{res_version}/{filename}"
    )

with open("assets.txt", "w") as f:
    for url in url_list:
        print(url, file=f)


subprocess.run(
    [
        "aria2c",
        "--allow-overwrite",
        "-d", f"assets/{res_version}/redirect/",
        "-i", "assets.txt"
    ]
)
