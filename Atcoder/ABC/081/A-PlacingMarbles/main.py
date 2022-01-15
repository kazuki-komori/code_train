
def get_value() -> str:
    return input()


def solution(s: [str]) -> int:
    print(s.count("1"))
    return s.count("1")


solution(get_value())
