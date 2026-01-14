n = 1000

for i in range(1, n + 1):
    num = i
    temp = i
    total = 0

    while num > 0:
        rem = num % 10
        total = (total * 10) + rem
        num = num // 10

    if total == temp:
        print("Palindrome =", temp)

    else:
        print("Not Palindrome =", temp)