#!/usr/bin/python3
"""Example of pycame usage."""

import logging
import sys

from pycame.came_manager import CameManager

DEBUG = False

HOST = "192.168.1.250"
USERNAME = "admin"
PASSWORD = "admin"
TOKEN = "your_access_token"


# Show debug logs to stdout
if DEBUG:
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Initialization of devices manager
manager = CameManager(HOST, USERNAME, PASSWORD, TOKEN)

# Print list of available devices
for device in manager.get_all_devices():
    print(
        f"Device type: {device.type},\tname: {device.name},\tstate: {device.state},\t"
        f"floor: {device.floor},\troom: {device.room}"
    )
