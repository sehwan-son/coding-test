def isLeapYear (year):
    if (year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
        return 1
    return 0

if __name__ == '__main__':
    year = int(input())
    print(isLeapYear(year))