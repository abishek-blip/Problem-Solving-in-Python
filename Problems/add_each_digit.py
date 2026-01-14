n = 0
total = 0

while n > 0:
    rem = n % 10
    total = total + rem
    n = n // 10

print(total)