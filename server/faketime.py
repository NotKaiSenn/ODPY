from constants import CONFIG_PATH
from utils import read_json
from time import time as real_time


def time():
    config = read_json(CONFIG_PATH)
    fakeTime = config["userConfig"]["fakeTime"]
    if fakeTime == -1:
        return real_time()
    return real_time() % (24*60*60) + fakeTime
