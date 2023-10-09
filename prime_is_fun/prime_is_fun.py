#main driver files: prime_is_fun.py
#Alejandro Rodriguez
#10/6/23

import prime

import matplotlib.pyplot as plt

import numpy as np

#promt user
print("Welcome to prime fun program")

#main loop
while True:
    
    #prompt user
    print("Enter 1 to start, or 0 to exit")

    n = int(input("choice: "))
    
    #user enters 0 break loop
    if n == 0:
        break
    
    #else continue
    else:
        
        #create list that points will go into
        x_points = []
        y_points = []
        
        # x will be form 1 to 100
        for x in range(0,101):
            
            #force x = 0, y = 0
            if x == 0:
                x_points.append(0)
                y_points.append(0)
            
            #force x = 1 , y = 0
            elif x == 1:
                x_points.append(1)
                y_points.append(0)
                
            #x = 2 till 100, y will be number of primes in x
            else:
                x_points.append(x)
                y_points.append(prime.Prime(x).number_primes())
        
        #initraize my graph with there points in 2 list
        plt.plot(x_points, y_points,"o")
        
        #give y axis a grid
        plt.grid(axis = 'y')
        
        #tick modifier -> min(start), max(end)+1 b/c of range stuff, step size
        plt.xticks(np.arange(min(x_points), max(x_points)+1, 5))
        plt.yticks(np.arange(min(y_points), max(y_points)+1, 1))
        
        #labels
        plt.title("number of primes n less then or equal to n")
        plt.xlabel("n")
        plt.ylabel("number of primes")
        
        #print graph
        plt.show()
        
    
    
    
