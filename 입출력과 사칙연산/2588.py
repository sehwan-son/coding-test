
def printMultiple (a, b):
    print(a * (b % 10))
    print(a * (int(b / 10) % 10))
    print(a * (int(b / 100) % 100))
    print(a * b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    printMultiple(a, b)