import os

from ppadb.client import Client
from datetime import datetime


def get_device_name(device):
    return device.get_properties()["ro.product.name"]


def get_datetime_from_device(device):
    return datetime.strptime(device.shell("date +%c"), '%c\n')


def get_timezone_from_device(device):
    return device.get_properties()["persist.sys.timezone"]


def get_localtime_from_device(device):
    return get_datetime_from_device(device).strftime("%H:%M:%S")


def print_devices_info(devices):
    if len(devices) == 0:
      print("No devices!")

    for device in devices:
        print(f"""
        Device: {get_device_name(device)}
            - Timezone: {get_timezone_from_device(device)}
            - Localtime: {get_localtime_from_device(device)}
        """)


if __name__ == '__main__':
    try:
        os.system("adb start-server")
        client = Client(host="localhost", port=5037)
        print_devices_info(client.devices())
    except Exception:
        print("Error starting adb server. Please be sure adb is installed.")

