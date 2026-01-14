num = 153
temp = num
result = 0

while num > 0:
    rem = num % 10
    # cube = rem * rem * rem
    cube = rem ** 3
    result = result + cube
    num = num // 10

if result == temp:
    print("Armstrong")

else:
    print("Not an Armstrong")