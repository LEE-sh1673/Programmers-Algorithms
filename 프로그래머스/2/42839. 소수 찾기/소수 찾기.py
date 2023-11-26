"""


"""
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True


def solution(numbers):
    prime_numbers = set()

    def make_comb(str1, str2):
        if str1 != "":
            num = int(str1)
            print(num)

            if is_prime(num):
                prime_numbers.add(num)

        for i in range(len(str2)):
            make_comb(str1 + str2[i], str2[:i] + str2[i + 1:])

    make_comb("", numbers)
    return len(prime_numbers)