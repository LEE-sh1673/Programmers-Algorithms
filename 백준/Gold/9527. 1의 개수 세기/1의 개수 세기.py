from sys import stdin


def one_count(num):  
    cnt = 0  
    bin_num = bin(num)[2:]  
    length = len(bin_num)
    
    for i in range(length):  
        if bin_num[i] == '1':    
            val = length - i - 1  
            cnt += dp[val] + (num - 2**val + 1)
            num -= 2 ** val
    return cnt

a, b = map(int, stdin.readline().split())
dp = [0] * 60

for i in range(1, 60):
    dp[i] = 2 * dp[i - 1] + 2 ** (i-1)

print(one_count(b) - one_count(a - 1))
