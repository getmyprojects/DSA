"""
problem is divided into sub-problems
apply memoization for repeated results

get fibonacci number
"""


# recursive
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

# DP
def fib_dp(n):
    f = [0] * (n+1)
    f[1] = 1

    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


if __name__ == "__main__":
    print(fib(6))
    print(fib_dp(6))