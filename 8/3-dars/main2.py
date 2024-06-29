# misol linki    https://www.codewars.com/kata/5e4e8f5a72d9550032953717/train/python

from collections import deque
from typing import Generator, Tuple


def all_rationals() -> Generator[Tuple[int, int], None, None]:
    queue = deque([(1, 1)])

    while True:
        a, b = queue.popleft()
        yield (a, b)
        queue.append((a, a + b))
        queue.append((a + b, b))


gen = all_rationals()
for _ in range(20):
    print(next(gen))
