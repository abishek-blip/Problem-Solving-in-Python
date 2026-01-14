num = [7,3,6,-256,-44,9,56]                                  #[5,5,5,5]

if len(num) < 2:
    print("Second maximum number not exist")

else:
    firstmax = float('-inf')
    secondmax = float('-inf')

    for i in range(0, len(num)):
        if (num[i] > firstmax):
            secondmax = firstmax
            firstmax = num[i]

        elif ((num[i] > secondmax) and (num[i] < firstmax)):
            secondmax = num[i]

    if(secondmax == float('-inf')):
        print("Second maximum number not exist")

    else:
        # print("First Maximum =", firstmax)
        print("Second Maximum =", secondmax)