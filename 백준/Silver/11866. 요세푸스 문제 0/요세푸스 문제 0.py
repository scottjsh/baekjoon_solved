import sys
from collections import deque

input = sys.stdin.readline

def josephus(N, K):
    queue = deque(range(1, N + 1))
    result = []
    
    while queue:
        # K-1 만큼 왼쪽으로 회전
        for _ in range(K - 1):
            queue.append(queue.popleft())
        # K번째 사람 제거
        result.append(queue.popleft())
    
    return result

# 입력 처리
N, K = map(int, input().strip().split())

# 요세푸스 순열 구하기
josephus_permutation = josephus(N, K)

# 출력 포맷에 맞게 출력
print("<" + ", ".join(map(str, josephus_permutation)) + ">")
