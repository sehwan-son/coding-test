import sys
input = sys.stdin.readline

if __name__ == '__main__':
    while(True):  
        A, B = map(int, input().split())
        if(A==0 and B==0):
            break
        print(A+B)
