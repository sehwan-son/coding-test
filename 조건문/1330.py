
def compare (A, B):
    if(A > B):
        print('>')
    elif(A < B):
        print('<')
    elif(A == B):
        print('==')

if __name__ == '__main__':
    A, B = map(int, input().split())
    compare(A, B)