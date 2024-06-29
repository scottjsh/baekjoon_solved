def reverse_binary(N):
    # 10진수 N을 이진수로 변환한 후 '0b'를 제거하고 뒤집기
    binary_str = bin(N)[2:][::-1]
    
    # 뒤집은 이진수를 다시 10진수로 변환
    reversed_decimal = int(binary_str, 2)
    
    return reversed_decimal

# 입력 받기
N = int(input())

# 결과 출력
print(reverse_binary(N))
