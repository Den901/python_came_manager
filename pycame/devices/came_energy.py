"""ETI/Domo Energy Measurament sensor device."""

import logging
from typing import Optional

from .base import TYPE_ENERGY_METER, CameDevice, DeviceState, StateType

_LOGGER = logging.getLogger(__name__)


    """ETI/Domo energy measurement device class."""

class CameeNERGYmETER(CameDevice):
  
    def __init__(self, manager, device_info: DeviceState):
        """Init instance."""
        super().__init__(manager, TYPE_ENERGY_METER, device_info)

    @property
    def current_consumption(self) -> float:
        """Get current consumption."""
        return self._device_info.get("current_consumption")

    @property
    def total_consumption(self) -> float:
        """Get total consumption."""
        return self._device_info.get("total_consumption")

    @property
    def last_consumption_update(self) -> datetime:
        """Get last consumption update."""
        return self._device_info.get("last_consumption_update")

    def update(self):
        """Update device state."""
        self._force_update("energy_measurement")


if __name__ == "__main__":

    # Create a CameManager instance.
    manager = CameManager()

    # Connect to the ETI/Domo server.
    manager.connect(ip_address="192.168.1.250", port=80, username="admin", password="admin")

    # Get the energy measurement device.
    device = manager.get_device(type_id=TYPE_ENERGY_METER)

    # Print the current consumption.
    print("Current consumption:", device.current_consumption)

    # Print the total consumption.
    print("Total consumption:", device.total_consumption)

    # Print the last consumption update.
    print("Last consumption update:", device.last_consumption_update)

    # Get the list of meters.
    meters = manager.get_meters()

    # Print the list of meters.
    for meter in meters:
        print(meter.id, meter.name, meter.type, meter.produced, meter.instant_power, meter.unit, meter.energy_unit)

    # Get the energy consumption data for a given meter.
    energy_consumption = manager.get_energy_consumption(meter_id=1, start_time="2023-08-11T00:00:00", end_time="2023-08-11T23:59:59")

    # Print the energy consumption data.
    for measurement in energy_consumption:
        print(measurement.power, measurement.delta_secs)

