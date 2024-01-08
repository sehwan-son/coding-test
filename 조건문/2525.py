def nMinAfter (n, H, M):
    return [(H + int((M + n) / 60)) % 24, (M + n) % 60]


if __name__ == '__main__':
    A, B = map(int, input().split())
    C = int(input())
    print(' '.join(map(str, nMinAfter(C, A, B))))