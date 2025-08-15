def second_max(arr):
    first_max = second = arr[0]
    
    for num in arr:
        if(num > first_max):
            second = first_max
            first_max = num
        elif num > second and num != first_max:
            second = num
    return second
n = int(input())
arr = list(map(int, input().split()))
res = second_max(arr)
print(res)