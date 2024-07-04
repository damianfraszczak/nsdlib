import cmath
import collections
from typing import Dict


def sort_dict_by_value(data: Dict[any, any], reverse=True) -> Dict[any, any]:
    """Sort a dictionary by its values."""
    return collections.OrderedDict(
        sorted(data.items(), key=lambda x: x[1], reverse=reverse)
    )


def normalize_dict_values(data: Dict[any, float]) -> Dict[any, float]:
    """Normalize dictionary values to the range [0, 1]."""
    if not data:
        return data
    data = {
        key: cmath.phase(value) if isinstance(value, complex) else value
        for key, value in data.items()
    }
    maxv = max(data.values())
    minv = min(data.values())
    divider = maxv - minv
    if divider == 0:
        divider = 1
    return {key: (value - minv) / divider for key, value in data.items()}
