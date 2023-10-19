#!/usr/bin/python3
"""Example of pycame usage."""

import logging
import sys
from time import sleep

from pycame.came_manager import CameManager

DEBUG = True

HOST = "192.168.1.250"
USERNAME = "admin"
PASSWORD = "admin"
TOKEN = "your_access_token"

OPENING_NAME = "Aperture motorizzate"


# Show debug logs to stdout
if DEBUG:
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Initialization of devices manager
manager = CameManager(HOST, USERNAME, PASSWORD, TOKEN)

print("Open the window")
manager.get_device_by_name(OPENING_NAME).open()

print("Wait for 5 seconds...")
sleep(5)

print("Stop the window")
manager.get_device_by_name(OPENING_NAME).stop()

print("Wait for 5 seconds...")
sleep(5)

print("Close the window")
manager.get_device_by_name(OPENING_NAME).close()
