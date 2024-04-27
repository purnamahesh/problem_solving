def fallingSum(inp: list[list[int]], n: int) -> int:
    def solve(i:int, j:int, val:int) -> int:
        if i >= n:
            return val
        elif j >= n or j < 0:
            return 99999999
        return min(
            solve(i+1, j - 1, val + inp[i][j]), 
            solve(i+1, j + 1, val + inp[i][j])
        )
    return min(solve(0,j,0) for j in range(n))

if __name__=='__main__':
    inp = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    n = 3
    print(fallingSum(inp, n))