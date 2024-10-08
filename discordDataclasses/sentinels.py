from __future__ import annotations

from typing import Any

"""Contains sentinels used in this package."""


class _MissingSentinel:
    """Borrowed from Rapptz/discord.py"""
    __slots__ = ()

    def __eq__(self, other) -> bool:
        return False

    def __bool__(self) -> bool:
        return False

    def __hash__(self) -> int:
        return 0

    def __repr__(self):
        return '...'


MISSING: Any = _MissingSentinel()


class _DeprecatedSentinel:
    """Denotes deprecated item"""
    __slots__ = ()

    def __eq__(self, other) -> bool:
        return False

    def __bool__(self) -> bool:
        return False

    def __hash__(self) -> int:
        return 0

    def __repr__(self):
        return '...'


DEPRECATED: Any = _DeprecatedSentinel()
