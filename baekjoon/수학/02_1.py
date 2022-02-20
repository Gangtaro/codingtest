import sys

def solution(n):
    num_len = len(str(n))
    while 1:
        if int('1' * num_len)%n == 0 : 
            break
        else : 
            num_len += 1
    print(num_len)
    return num_len

if __name__ == '__main__'  :
    while True : 
        try : 
            n = int(sys.stdin.readline())
            solution(n)
        except :
            break

