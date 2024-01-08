
# 한 줄에 여러 개의 숫자 입력 받기
a, b, c, d = map(int, input().split())
print(a, b, c, d)


# 리스트 원소 한 줄로 입력 받기
'''
1 3 5 7 9
'''
a = list(map(int, input().split()))
print(a) # [1, 3, 5, 7, 9]

'''
A B C D E
'''
a = list(input().split())



# 2차원 리스트 입력 받기
'''
[입력 예시]
5
0 2 1 1 0
1 1 1 1 2
0 2 1 2 1
0 2 1 1 0
0 1 1 1 2
'''

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))