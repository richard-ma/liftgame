#!/usr/bin/env python3

import json
from .world import World


class WorldHistory:
    def __init__(self) -> None:
        self._history = list()

    def append_history(self, world: World) -> None:
        self._history.append(world.get_alive())

    def _clear(self) -> None:
        self._history = list()

    def clear_history(self) -> None:
        self._clear()

    def len(self) -> int:
        return len(self._history)

    def get(self, index: int) -> World:
        return World(self._history[index])

    def get_first(self) -> World:
        return self.get(0)

    def get_last(self) -> World:
        return self.get(-1)

    def save(self, record_filename) -> bool:
        serialized_history = json.dumps(self._history)
        with open(record_filename, 'w') as file:
            file.write(serialized_history)
        return True

    def load(self, record_filename) -> bool:
        serialized_history = ""
        with open(record_filename, 'r') as file:
            serialized_history = file.read()
        self._history = json.loads(serialized_history)
        return True