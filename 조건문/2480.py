def priceOf (a, b, c):
    if (a == b == c):
        return 10000 + a * 1000
    elif (a == b or b == c):
        return 1000 + b * 100
    elif (c == a):
        return 1000 + c * 100
    else:
        return max(a, b, c) * 100


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(priceOf(a, b, c))