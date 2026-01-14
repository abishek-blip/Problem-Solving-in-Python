n = 10

start = 0
next = 1

if (n <= 0):
    print("invalid number for fibonacci series")

else:
    for i in range(1, n + 1):
        print(start,end="  ")
        temp = start
        start = next
        next = temp + next