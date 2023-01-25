def solution(arr):
    new_arr = []
    new_arr.append(arr[0])
    
    for i in arr[1:]:
        if i != new_arr[-1]:
            new_arr.append(i)
    return new_arr