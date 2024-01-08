def nMinAgo (n, H, M):
    if(M - n < 0):
        if (H == 0):
            return [23, 60 + M - n]
        return [H - 1,  60 + M - n]
    
    return [H, M - n]

if __name__ == '__main__':
    H, M = map(int, input().split())
    print(' '.join(map(str, nMinAgo(45, H, M))))