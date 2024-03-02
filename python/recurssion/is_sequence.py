from typing import List

def is_sequence(arr: List[int]):
    n = len(arr)
    def solve(arr: List[int], indx: int):
        if indx == n:
            return True
        return solve(arr, indx+1) if arr[indx-1] == arr[indx]-1 else False
    return solve(arr, 1)

if __name__ == '__main__':
    # arr = [1,2,3,4,5,6]
    arr = [1,2,3,4,6]
    print(
        f"Array:{arr} is{'' if is_sequence(arr) else ' not'} in sequence!"
    )