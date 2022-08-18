def average(arr):
    full_len: int = len(arr)
    sum = 0
    for i in arr:
        sum += i
    answer = sum / full_len
    return answer

a = [1,2,3,4]

print(average(a))
