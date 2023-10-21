"""ETI/Domo devices subpackage."""

import logging
from typing import List

from pycame.devices.came_analog_sensor import CameAnalogSensor
from pycame.devices.came_energy_sensor import CameEnergySensor

from .base import CameDevice
from .came_light import CameLight
from .came_thermo import CameThermo
from .came_relay import CameRelay
from .came_opening import CameOpening

_LOGGER = logging.getLogger(__name__)

def get_featured_devices(manager, feature: str) -> List[CameDevice]:
    """Get device implementations for the given feature."""
    devices = []

    if feature == "lights":
        cmd = {
            "cmd_name": "light_list_req",
            "topologic_scope": "plant",
        }
        response = manager.application_request(cmd, "light_list_resp")

        for device_info in response.get("array", []):
            devices.append(CameLight(manager, device_info))

        return devices

    if feature == "openings":
        cmd = {
            "cmd_name": "openings_list_req",
            "topologic_scope": "plant",
        }
        response = manager.application_request(cmd, "openings_list_resp")

        for device_info in response.get("array", []):
            devices.append(CameOpening(manager, device_info))

        return devices

    if feature == "relays":
        cmd = {
            "cmd_name": "relays_list_req",
            "topologic_scope": "plant",
        }
        response = manager.application_request(cmd, "relays_list_resp")

        for device_info in response.get("array", []):
            devices.append(CameRelay(manager, device_info))

        return devices

    if feature == "thermoregulation":
        cmd = {
            "cmd_name": "thermo_list_req",
            "topologic_scope": "plant",
        }
        response = manager.application_request(cmd, "thermo_list_resp")

        for device_info in response.get("array", []):
            devices.append(CameThermo(manager, device_info))

        for sensor in ["temperature", "humidity", "pressure"]:
            res = response.get(sensor)
            if res is not None:
                devices.append(
                    CameAnalogSensor(
                        manager, res, "thermo", sensor, device_class=sensor
                    )
                )

        return devices

    if feature == "energy":
    cmd = {
        "cmd_name": "meters_list_req",
        "topologic_scope": "plant",
    }
    response = manager.application_request(cmd, "meters_list_resp")

    for meter_data in response.get("array", []):
        devices.append(CameEnergySensor(manager, meter_data))

        return devices

                        
