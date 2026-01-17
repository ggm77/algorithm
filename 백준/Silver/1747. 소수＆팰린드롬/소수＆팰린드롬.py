def is_palindrome(n):
    s = str(n)
    for i in range(int(len(s)/2)):
        if(s[i] != s[len(s)-i-1]):
            return False
    return True


n = int(input())

if(n <= 2):
    print("2")
elif(n == 3):
    print("3")
else:
    prime_num = [0] * 1500001

    for i in range(2, 1500000):
        if(prime_num[i] != 1):
            for j in range(2, int(1500001/i)+1):
                if(i*j < 1500000):
                    prime_num[i*j] = 1
            if(n <= i and is_palindrome(i)):
                print(i)
                break
