n = int(input())
x = 0

for _ in range(n):
    statement = input().strip()

    if "++" in statement:
        x = x + 1
    else:
        x = x - 1

print(x)        