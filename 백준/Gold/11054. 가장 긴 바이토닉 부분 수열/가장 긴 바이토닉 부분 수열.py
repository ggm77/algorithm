import sys
input = sys.stdin.readline

"""

dp1 : 앞에서부터, 마지막 값을 무조건 사용하는 증가하는 부분 수열
dp2 : 뒤에서부터, 마지막 값을 무조건 사용하는 감소하는 부분 수열

"""

n = int(input().rstrip())

arr = [0]
arr += list(map(int, input().split()))

if(n == 1):
    print("1")
else:
    dp1 = [0] * (n+1)
    dp2 = [0] * (n+1)

    dp1[1] = 1
    dp2[1] = 1

    for i in range(2, n+1):
        smaller_val_cnt_1 = -1
        smaller_val_cnt_2 = -1
        smaller_val_index1 = -1
        smaller_val_index2 = -1

        for j in range(i-1, 0, -1):
            if(arr[j] < arr[i] and smaller_val_cnt_1 < dp1[j]):
                smaller_val_cnt_1 = dp1[j]
                smaller_val_index1 = j
            if(arr[j*-1] < arr[i*-1] and smaller_val_cnt_2 < dp2[j]):
                smaller_val_cnt_2 = dp2[j]
                smaller_val_index2 = j
        
        if(smaller_val_index1 != -1):
            dp1[i] = dp1[smaller_val_index1] + 1
        else:
            dp1[i] = 1
        
        if(smaller_val_index2 != -1):
            dp2[i] = dp2[smaller_val_index2] + 1
        else:
            dp2[i] = 1
        
    result = -1
    for i in range(1, n+1):
        if(result < dp1[i] + dp2[n-i+1] - 1):
            result = dp1[i] + dp2[n-i+1] - 1

    print(result)