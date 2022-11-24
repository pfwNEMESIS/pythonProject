from typing import List, Union, Optional


def calc(a: Optional[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


def to_int(a_list: List[str]) -> List[int]:
    return [int(e) for e in a_list]


if __name__ == '__main__':
    calc([1.2, 2.3])
