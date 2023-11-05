import os
import sys
import subprocess
from contextlib import suppress
import json

from ppadb.client import Client as AdbClient

server_port = json.load(open('./config/config.json', 'r'))["server"]["port"]
default_ports = [7555, 5555, 62001]
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

    devices = client.devices()
    if len(devices) == 1:
        return devices[0]

os.system('cls')
# subprocess.run(f'"{ADB_PATH}" kill-server')
subprocess.run(f'"{ADB_PATH}" start-server')
    
client = AdbClient(host="127.0.0.1", port=5037)
device = None

print("Trying to connect to currently opened emulator")
device = get_device()

print("Check the emulator and accept if it asks for root permission.")
with suppress(RuntimeError):
    device.root()
device = get_device()
os.system(f'"{ADB_PATH}" wait-for-device')

print("\nRunning frida\nNow you can start fridahook\n")
os.system(f'"{ADB_PATH}" reverse tcp:{server_port} tcp:{server_port}')
os.system(f'"{ADB_PATH}"' + " shell /data/local/tmp/frida-server &")
