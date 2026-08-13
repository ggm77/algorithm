def solution(nums):
    answer = 0

    primes = [2, 3, 5]
    
    for i in range(6, 3000):
        isPrime = True
        for j in primes:
            if (i%j == 0):
                isPrime = False
            if (not isPrime):
                break
                
        if (isPrime):
            primes.append(i)
            

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (nums[i]+nums[j]+nums[k] in primes):
                    answer += 1
    
    return answer