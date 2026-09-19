# type annotations in python
def calculate(a: int, b: int) -> int:
    return a + b


def calc(a: int, b: int) -> None:
    print(a + b)


def max_marks(marks: list[int]) -> int:
    return max(marks)


ans = max_marks([89, True, 90, "anirudh"])
