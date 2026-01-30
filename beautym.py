r = 0
c = 0

for i in range(5):
    row = input().split()   
    for j in range(5):
        if int(row[j]) == 1:
            r = i + 1      
            c = j + 1

moves = abs(r - 3) + abs(c - 3)

print(moves)
