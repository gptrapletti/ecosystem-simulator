import random
from typing import List, Any


def shuffle_list(ls: List[Any]) -> List[Any]:
    idxs = list(range(len(ls)))
    random.shuffle(idxs)
    return [ls[i] for i in idxs]