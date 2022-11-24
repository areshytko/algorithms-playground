from typing import List, Tuple

from algoutils import main, log


def union_find(size: int, edges: List[Tuple[int, int]], element_a: int, element_b: int):
    pass


class UnionFind:

    def __init__(self, size: int, edges: List[Tuple[int, int]]):
        self.tree_array = list(range(size))
        for el_a, el_b in edges:
            self.union(el_a, el_b)

    def union(self, element_a: int, element_b: int):
        log("ssss")
        pass

    def find(self, element: int) -> int:
        pass

    def connected(self, element_a: int, element_b: int) -> bool:
        return self.find(element_a) == self.find(element_b)


if __name__ == '__main__':
    main(union_find)
