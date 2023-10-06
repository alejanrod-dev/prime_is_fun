#main driver
#Alejandro Rodriguez
#10/6/23

import prime

#promt user
print("Welcome to prime fun program")

#main loop
while True:
    
    #prompt user
    print("Enter your n. or 0 to exit")

    n = int(input("choice: "))
    
    #user enters 0 break loop
    if n == 0:
        break
    
    #else continue
    else:
        
        #x is equal to prome object with attribute n
        x = prime.Prime(n)
        
        #hold number of primes <= n
        number_of_primes = x.number_primes()
        
        print(number_of_primes)
    
    
    
