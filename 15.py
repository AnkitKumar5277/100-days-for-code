# Python program to display all the prime numbers within an interval
lower = 900
upper = 1000
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
# Prime numbers between 900 and 1000 are:
# 907
# 911
# 919
# 929
# 937
# 941
# 947
# 953
# 967
# 971
# 977
# 983
# 991
# 997

def is_prime_in_range(number, start, end):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    # Check divisors in the specified range
    for divisor in range(start, end + 1):
        if divisor > 1 and divisor < number and number % divisor == 0:
            return False  # Divisible within range; not prime
    return True
# Example usage
result = is_prime_in_range(49, 2, 6)
print(result) 
# Output: True
