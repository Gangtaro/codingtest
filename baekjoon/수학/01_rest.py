import sys
a, b, c = map(int,sys.stdin.readline().split())

def solution(a, b, c):
    print((a+b)%c)
    print(((a%c) + (b%c))%c)
    print((a*b)%c)
    print(((a%c) * (b%c))%c)

if __name__ == '__main__'  :
    solution(a, b, c)




