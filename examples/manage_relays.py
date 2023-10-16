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

RELAY_NAME = "Attivazione"


# Show debug logs to stdout
if DEBUG:
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Initialization of devices manager
manager = CameManager(HOST, USERNAME, PASSWORD, TOKEN)

print("Turn on relay")
manager.get_device_by_name(RELAY_NAME).turn_on()

print("Wait for 10 seconds...")
sleep(10)

print("Turn off light")
manager.get_device_by_name(RELAY_NAME).turn_off()

print("Wait for 10 seconds...")
sleep(10)
