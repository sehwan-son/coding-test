import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        A, B = map(int, input().rstrip().split())
        print(A+B)