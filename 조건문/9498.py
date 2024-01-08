def gradeOf (score):
    if (90 <= score <= 100):
        return 'A'
    elif (80 <= score < 90):  
        return 'B'
    elif (70 <= score < 80):
        return 'C'
    elif (60 <= score < 70):
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    score = int(input())
    print(gradeOf(score))