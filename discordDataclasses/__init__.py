from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import List, Type, TypeVar, Any

from . import *

"""Defines the main module"""

T = TypeVar('T')  # Generic type


def from_dict(cls: Type[T], data: dict) -> T:
    """Instantiates a class from a dictionary"""
    if not is_dataclass(cls):
        raise TypeError(f"{cls.__name__} is not a dataclass")

    kwargs = {}

    for field in fields(cls):
        field_value = data.get(field.name)

        if isinstance(field_value, list) and hasattr(field.type, '__origin__') and issubclass(field.type.__origin__,
                                                                                              list):
            sub_cls = field.type.__args__[0]
            kwargs[field.name] = [from_dict(sub_cls, item) for item in field_value]
        elif is_dataclass(field.type):
            kwargs[field.name] = from_dict(field.type, field_value)
        else:
            kwargs[field.name] = field_value

    return cls(**kwargs)
