def printMultiplicationTableOf (N):
    for i in list(range(1,10)):
        print(N, "*", i, "=", N * i)


if __name__ == '__main__':
    N = int(input())
    printMultiplicationTableOf(N)