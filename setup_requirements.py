import os
import sys
import lzma
import subprocess
from zipfile import ZipFile
from contextlib import suppress

import requests
from ppadb.client import Client as AdbClient

ADB_PATH = "platform-tools\\adb.exe"

def get_device():
    devices = client.devices()
    if len(devices) == 0:
        for port in default_ports:
            with suppress(Exception):
                client.remote_connect("127.0.0.1", port)
                devices = client.devices()
                if len(devices) == 1:
                    return devices[0]
        
        print("No emulator found.\nEnter the adb connection url with port manually or type q to exit or press enter to wait for a device: ")
        result = input()
        if result.lower() == "q":
            sys.exit(0)
        
        if result:
            result = result.split(":")
            client.remote_connect(result[0], int(result[1]))

    result = subprocess.getoutput(f'"{ADB_PATH}" wait-for-device')
    devices = client.devices()
    if len(devices) == 1:
        return devices[0]

if not os.path.exists(ADB_PATH):
    if not os.path.exists("adb.zip"):
        print("No adb file found. Downloading the latest version.")
        r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-windows.zip", allow_redirects=True)
        open('adb.zip', 'wb').write(r.content)
    ZipFile('adb.zip').extractall(".")

os.system('cls')
subprocess.run(f"{ADB_PATH} kill-server")
subprocess.run(f"{ADB_PATH} start-server")
default_ports = [7555, 62001]
client = AdbClient(host="127.0.0.1", port=5037)
device = None

print("Trying to connect to currently opened emulator")
device = get_device()

print("Check the emulator and accept if it asks for root permission.")
with suppress(RuntimeError):
    device.root()
device = get_device()
os.system(f'{ADB_PATH} wait-for-device')

frida_exists = device.shell('test -f /data/local/tmp/frida-server && echo True').strip()
if not frida_exists:
    architecture = device.shell("getprop ro.product.cpu.abi").strip().replace("-v8a", "")
    print(f"\nArchitecture: {architecture}")

    if not os.path.exists(f"frida-server-{architecture}.xz"):
        version = requests.get("https://api.github.com/repos/frida/frida/releases/latest").json()["tag_name"]
        name = f"frida-server-{version}-android-{architecture}"
        print(f"Downloading {name}...")
        url = f"https://github.com/frida/frida/releases/download/{version}/{name}.xz"
        r = requests.get(url, allow_redirects=True)
        open(f"frida-server-{architecture}.xz", 'wb').write(r.content)

    print("Extracting....")
    with lzma.open(f"frida-server-{architecture}.xz") as f, open('frida-server', 'wb') as fout:
        file_content = f.read()
        fout.write(file_content)

    print("Copying frida-server...")
    device.push("frida-server", "/data/local/tmp/frida-server")

    print("Modifying permissions")
    device.shell("chmod 755 /data/local/tmp/frida-server")
    os.remove("frida-server")

    print("\nFrida-server is installed!")

input("Press enter to exit...")