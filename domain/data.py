from abc import ABCMeta
from dataclasses import dataclass, field
import numpy as np


@dataclass
class Data:
    __metadata__ = ABCMeta

    data: np.array
    name: str = field(default=None)
    details: str = field(default=None)
