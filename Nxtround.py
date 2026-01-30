n, k = input().split()
n = int(n)
k = int(k)

scores_str = input().split()
scores = []

for s in scores_str:
    scores.append(int(s))

threshold = scores[k - 1]

count = 0
for score in scores:
    if score >= threshold and score > 0:
        count += 1

print(count)
