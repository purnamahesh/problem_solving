from random import randint

arr = [*map(lambda x: randint(x,100),range(10))]

def maximum(arr):
    def solve(arr, indx, max):
        if indx==-1:
            return max
        return solve(arr, indx - 1, arr[indx] if arr[indx] > max else max)
    return solve(arr, len(arr)-1, -1)

print(
    f"Maxmium element in arr {arr} is {maximum(arr)}"
)