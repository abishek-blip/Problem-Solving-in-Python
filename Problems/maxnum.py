number = [10, 25, 7, 18, 93]
max = number[0]

for i in range(0, len(number)):
    if(number[i] > max):
        max = number[i]

print("Maximum number in this list is", max)