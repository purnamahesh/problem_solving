from random import randint
from typing import List

def maximum(arr: List[int]) -> bool:
    def solve(arr: List[int], indx: int, max: int):
        if indx==-1:
            return max
        return solve(arr, indx - 1, arr[indx] if arr[indx] > max else max)
    return solve(arr, len(arr)-1, -1)

if __name__ == '__main__':
    arr: List[int] = [*map(lambda _: randint(0,100),range(10))]
    print(
        f"Maxmium element in arr {arr} is {maximum(arr)}"
    )