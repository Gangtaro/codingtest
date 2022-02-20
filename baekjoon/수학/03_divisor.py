import sys
num = int(sys.stdin.readline())
divisors = list(map(int,sys.stdin.readline().split()))

def solution(num, divisors):
    '''
    input: 
        num : (int) The number of real divisor of N
        divisors: (list, int) The list of real divisor of N
    output:
        N
    '''
    N = max(divisors)*min(divisors)
    print(N)
    return

if __name__ == '__main__' :
    solution(num, divisors)
