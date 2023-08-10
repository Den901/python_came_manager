# ETI/Domo opening device.

import logging
from typing import List

from .base import TYPE_OPENING, CameDevice, DeviceState

_LOGGER = logging.getLogger(__name__)

# Opening states
OPENING_STATE_CLOSED = 0
OPENING_STATE_OPEN = 1

class CameOpening(CameDevice):
    """ETI/Domo opening device class."""

    def __init__(self, manager, device_info: DeviceState):
        """Init instance."""
        super().__init__(manager, TYPE_OPENING, device_info)

    @property
    def opening_state(self) -> int:
        """Get the state of the opening."""
        return self._device_info.get("status")

    def open(self):
        """Open the opening."""
        self.move(OPENING_STATE_OPEN)

    def close(self):
        """Close the opening."""
        self.move(OPENING_STATE_CLOSED)

    def move(self, state: int):
        """Move the opening to a specific state."""
        if state not in [OPENING_STATE_CLOSED, OPENING_STATE_OPEN]:
            raise ValueError("Invalid state value")

        self._check_act_id()

        cmd = {
            "cmd_name": "opening_move_req",
            "act_id": self.act_id,
            "wanted_status": state,
        }

        _LOGGER.debug('Moving opening "%s" to state: %s', self.name, state)

        self._manager.application_request(cmd)

    def update(self):
        """Update device state."""
        self._force_update("opening")

    # ... (other methods if present)

