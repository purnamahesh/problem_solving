from typing import List

def is_sorted(arr: List[int]) -> bool:
    n: int = len(arr)
    def solve(arr: List[int], indx: int, prev: int):
        if indx == n:
            return True
        return False if prev > arr[indx] else solve(arr, indx+1, arr[indx])
    return solve(arr, 0, -1)

if __name__ == '__main__':
    from random import randint
    is_asc: int = randint(0,1)
    start: int = randint(1, 1000)
    step: int = randint(1,20)
    arr: List[int] = [*range(start, start+100, step)]
    
    if not is_asc:
        arr = arr[::-1]
    print(
        f"Array:{arr} is{'' if is_sorted(arr) else ' not'} sorted!"
    )