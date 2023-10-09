#object class with functions related to prime numbers
#Alejandro Rodriguez
#10/6/23

import math



class Prime():
    
    def __init__(self,n):
        #take n input
        self.n = n
        
    def print_n(self):
        #simple print of artribute n
        print(self.n)
        
    #check if given attribute n is prime
    def attribute_prime_check(self):
        
        is_prime = True
        
        #equal to the int value of sprt(n)
        check = int(math.sqrt(self.n))
        
        #will iterate thru all integers 2 -> check
        for x in range(2,check+1):
            
            #if n divides x, then n is not prime, return not prime!
            if self.n % x == 0:
                is_prime = False
                break
        
        #print("is prime ",is_prime)
        return is_prime
    
    #checks if given a is prime
    def prime_checker(self,a):
        
        is_prime = True
        
        #equal to the int value of sprt(n)
        check = int(math.sqrt(a))
        
        #will iterate thru all integers 2 -> check
        for x in range(2,check+1):
            
            #if q divides x, then a is not prime, return not prime!
            if a % x == 0:
                is_prime = False
                break
        
        return is_prime
    
    def number_primes(self):
        
        #create empty list that will hold prime numbers less then n
        prime_list = []
        
        #itterate thru all integers 2 -> n
        for x in range(2,self.n):
            
            #if n is prime, add n to list of primes
            if self.prime_checker(x) == True:
                prime_list.append(x)
                
        #print(prime_list)

        #return lenth of list of primes
        return len(prime_list)
                

                
        
        
        
        

