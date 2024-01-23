N = int(input())
S = input()
for c in S:
    x = ord(c) - ord('A')
    x = (x + N) % 26
    print(chr(x + ord('A')), end='')
