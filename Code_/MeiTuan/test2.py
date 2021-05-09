a, b, c = list(map(int, input().split()))
pow_A, pow_B = 0, 0
for i in range(a):
    x, y = list(map(int, input().split()))
    if y >= c:
        pow_A += x * y
for i in range(b):
    x, y = list(map(int, input().split()))
    if y >= c:
        pow_B += x * y
print(pow_A, pow_B)
if pow_A > pow_B:
    print('A')
else:
    print('B')
