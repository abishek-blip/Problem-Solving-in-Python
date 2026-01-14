num = 12321
temp = num
result = 0

while num > 0:
    rem = num % 10
    result = result * 10 + rem
    num = num // 10

if result == temp:
    print("Palindrome")

else:
    print("Not a Palindrome")