number = [10, 0, 7, 18, 93]
min = number[0]

for i in range(0, len(number)):
    if(number[i] < min):
        min = number[i]

print("Minimum number in this list is", min)