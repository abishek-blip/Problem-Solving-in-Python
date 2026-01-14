n = 8676
result = 0
while n > 0:
    # rem = n % 10
    result = (result * 10) + (n % 10)
    n = (int)(n / 10)

print(result)