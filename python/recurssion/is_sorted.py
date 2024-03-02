arr = [1,2,3,4,5,7,6]

def is_sorted(arr):
    n = len(arr)
    def solve(arr, indx, prev):
        if indx == n:
            return True
        return False if prev > arr[indx] else solve(arr, indx+1, arr[indx])
    return solve(arr, 0, -1)

print(
    f"Array:{arr} is{'' if is_sorted(arr) else ' not'} sorted!"
)