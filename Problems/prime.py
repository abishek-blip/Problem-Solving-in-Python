num = -6

if (num >= 2):
    isprime = True

    for i in range(2, num):
        if(num % i == 0):
            isprime = False
            break

    if(isprime == True):
        print("Prime")

    else:
        print("Not Prime")

else:
    print("Not Prime")