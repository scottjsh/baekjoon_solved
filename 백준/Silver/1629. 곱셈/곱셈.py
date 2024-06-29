import sys
input = sys.stdin.read

# 입력 받기
A, B, C = map(int, input().strip().split())

# A를 B번 곱한 후 C로 나눈 나머지 계산
result = pow(A, B, C)

# 결과 출력
print(result)
