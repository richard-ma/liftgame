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