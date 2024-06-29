import sys

def is_palindrome(s):
    return s == s[::-1]

input = sys.stdin.read().strip().splitlines()
results = []

for line in input:
    num = line.strip()
    if num == '0':
        break
    if is_palindrome(num):
        results.append('yes')
    else:
        results.append('no')

for result in results:
    print(result)
