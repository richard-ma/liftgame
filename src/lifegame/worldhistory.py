#!/usr/bin/env python3


class WorldHistory:
    def __init__(self) -> None:
        self._history = list()

    def append_history(self, world: World) -> None:
        self._history.append(world)

    def _clear(self) -> None:
        self._history = list()

    def clear_history(self) -> None:
        self._clear()