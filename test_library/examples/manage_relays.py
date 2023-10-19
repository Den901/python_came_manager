#!/usr/bin/python3
"""Example of pycame usage."""

import logging
import sys
from time import sleep

from pycame.came_manager import CameManager

DEBUG = True

HOST = "192.168.3.6"
USERNAME = "admin"
PASSWORD = "admin"
TOKEN = "dregdrt94985492"

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

print("Turn off relay")
manager.get_device_by_name(RELAY_NAME).turn_off()

print("Wait for 10 seconds...")
sleep(10)
