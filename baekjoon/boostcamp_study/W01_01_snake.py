# Input
import sys
N = int(sys.stdin.readline()) # 보드의 크기
K = int(sys.stdin.readline()) # 사과의 개수
apple_location = []
for _ in range(K):
    apple_location.append( tuple(map(int, sys.stdin.readline().split())) )
L = int(sys.stdin.readline()) # 뱀의 이동횟수
snake_move = []
for _ in range(L):
    snake_move.append( tuple(map(str, sys.stdin.readline().split())) )
snake_move = [ (int(t), str(w)) for t, w in snake_move ]

# algo
# 선입후출 구조 -> 큐
from collections import deque
def solution(N, K, apple_location, L, snake_move):

    di, dj = 0, 1 # initial direction is right side
    total_time = 0
    queue = deque()
    i, j = (1, 1) # initial snake's head loc
    queue.append((i, j)) # initial snake
    last_times = 0
    snake_move.append((10001, 'END'))

    for times, turn in snake_move:
        now_times = times - last_times
        last_times = times
        print(f'=-=-=-= times: {now_times} =-=-=-=')
        
        for t in range(now_times):
            total_time += 1
            # x, y = head
            i, j = i + di, j + dj # move head's location
            print('HEAD:', (i, j), ' | before queue: ', queue)
            # --- (1) is there WALL? ---
            if i < 1 or i > N or j < 1 or j > N:
                print('==== activate condition 1 break point: WALL ====')
                print('queue: ', queue)
                print('total_time: ', total_time)
                return total_time

            # --- (2) is there your body? ---
            if (i, j) in queue:
                print('==== activate condition 2 break point: BODY ====')
                print('queue: ', queue)
                print('total_time: ', total_time)
                return total_time

            # --- (3) is there apple? ---
            if (i, j) in apple_location:
                print('@@@ EAT APPLE @@@')
                apple_location.remove((i, j))
                
                # don't use popleft
                queue.append((i, j))
                # continue

            else : 
                queue.append((i, j))
                queue.popleft() 

        # direction update (next direction)
        di, dj = (dj, -di) if turn == 'D' else (-dj, di)
        print(f'turn to {(di, dj)}')
        print()

    return total_time

# Output
if __name__ == '__main__'  :
    print("----input----")
    print("보드의 크기:", N)
    print("사과의 개수:", K)
    print("사과의 위치:", apple_location)
    print("뱀의 이동횟수:", L)
    print("뱀의 이동경로:", snake_move)
    print()
    print("----output----")
    print(solution(N, K, apple_location, L, snake_move))