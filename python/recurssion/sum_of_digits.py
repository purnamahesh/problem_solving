def sum_of_digits(n: int, sum: int = 0):
    return sum if n==0 else sum_of_digits(n//10,sum + n%10)

if __name__ == '__main__':
    from random import randint
    x:int = randint(9999,99999999)
    print(
        f"{x=} {sum_of_digits(x)=}"
    )