from typing import Tuple


def solve(n1: int, n2: int) -> str:
    time = n1 * n2
    if time % 2 == 0:
        print("Even")
        return "Even"
    else:
        print("Odd")
        return "Odd"


def get_value() -> Tuple[int, int]:
    n1, n2 = map(int, input().split())
    return n1, n2


n1, n2 = get_value()
solve(n1, n2)
