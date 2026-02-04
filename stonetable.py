n = int(input("Enter number of stones (1 to 50): "))

if n < 1 or n > 50:
    print("Invalid n. Must be between 1 and 50.")
    exit()

stones = input("Enter stone colors (R, G, B): ")

if len(stones) != n:
    print("Invalid input length.")
    exit()

remove_count = 0

for i in range(1, n):
    if stones[i] == stones[i - 1]:
        remove_count += 1

remaining = n - remove_count

print("Stones remaining:", remaining)

