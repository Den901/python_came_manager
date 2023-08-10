import logging
from typing import List, Optional

_LOGGER = logging.getLogger(__name__)

class OpeningEntity:
    def __init__(self, manager, opening_info):
        self._manager = manager
        self._opening_info = opening_info

    @property
    def name(self) -> str:
        return self._opening_info.get("name", "Unknown Opening")

    @property
    def act_id_open(self) -> int:
        return self._opening_info.get("act_id_open", -1)

    @property
    def act_id_close(self) -> int:
        return self._opening_info.get("act_id_close", -1)

    @property
    def floor_index(self) -> int:
        return self._opening_info.get("floor_ind", -1)

    @property
    def room_index(self) -> int:
        return self._opening_info.get("room_ind", -1)

    @property
    def status(self) -> int:
        return self._opening_info.get("status", -1)

    @property
    def partial_commands(self) -> List[dict]:
        return self._opening_info.get("partial", [])

    def open(self):
        self._move(1)

    def close(self):
        self._move(2)

    def _move(self, wanted_status):
        self._manager.opening_move_req(self.act_id_open, wanted_status)

    def __str__(self):
        return f"OpeningEntity(name={self.name}, status={self.status})"

    def __repr__(self):
        return str(self)
