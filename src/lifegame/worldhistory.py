#!/usr/bin/env python3

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

    def get_lasst(self) -> World:
        return self.get(-1)

    def save(self, record_filename) -> bool:
        return True

    def load(self, record_filename) -> bool:
        return True