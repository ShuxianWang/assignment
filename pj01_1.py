from math import sqrt
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

if __name__ =='__main__':
    n=1000000
    s=0
    for i in range(1000,n+1):
        if is_prime(i)*is_prime(i+2):
            s= s + 1
    print('The total number of twim primes between 1 thousand and 1 million is %d',s)
    
#The total number of twim primes between 1 thousand and 1 million is %d 8134
