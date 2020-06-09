import time
# start = time.time()
def fibo_even_sum(num):
    arr = []
    sum = 0
    i = 0
    if num >= 1:
        arr.append(1)
        i+=1
    if num >= 2:
        arr.append(2)
        i+=1
    if num >= 3:
        while arr[i - 1] + arr[i - 2] <= num:
            arr.append(arr[i - 1] + arr[i - 2])
            i += 1
    for j in range(i):
        if arr[j] % 2 == 0:
            sum += arr[j]
    return sum
    
for i in range(int(input())):
    print(fibo_even_sum(int(input())))
end = time.time()
print(" %s seconds" %(end - start))
# # 6.6534371376 seconds for 100