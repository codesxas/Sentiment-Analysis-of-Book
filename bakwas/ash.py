l, r, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
arr = [i for i in range(l, r+1)]

count = 0
min_x = min(a)
for i in range(len(arr)):
    diff = arr[i] + min_x
    if diff in arr:
        count = count + (r - diff) + 1
        print("diff", diff)
        print(count)
    else:
        break
        
        
print(count)

