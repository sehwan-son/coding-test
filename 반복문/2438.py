import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    for i in range(1, N + 1):
        print('*'*i)