n = 20

for i in range(1, n + 1):
    
    if(i < 2):
        print(i,"-> Not Prime")
        
    else:
        isprime = True
        reduce_iter = int(i ** 0.5) + 1    #root level reducing for optimal solution(reduces iteration)

        for j in range(2, reduce_iter):
            if(i % j == 0):
                isprime = False
                break

        if(isprime == True):
            print(i,"-> Prime")

        else:
            print(i,"-> Not Prime")
