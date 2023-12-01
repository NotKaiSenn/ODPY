import requests

try:
    r = requests.get(
        "https://dl.google.com/android/repository/platform-tools-latest-windows.zip", allow_redirects=True
    )
    with open("adb.zip", "wb") as f:
        f.write(r.content)
except Exception:
    pass


try:
    architectures = ["x86_64"]
    for architecture in architectures:
        version = requests.get(
            "https://api.github.com/repos/frida/frida/releases/latest"
        ).json()["tag_name"]
        name = f"frida-server-{version}-android-{architecture}"
        url = f"https://github.com/frida/frida/releases/download/{version}/{name}.xz"
        r = requests.get(url, allow_redirects=True)
        with open(f"frida-server-{architecture}.xz", "wb") as f:
            f.write(r.content)
except Exception:
    pass
