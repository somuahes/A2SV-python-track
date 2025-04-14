n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = []
j = 0
for num in b:
    while j < n and a[j] < num:
        j += 1
    count.append(j)
print(" ".join(map(str, count)))
