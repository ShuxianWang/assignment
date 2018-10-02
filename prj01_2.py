from math import sqrt
import sys
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

if __name__ =='__main__':
    i=sys.maxsize
    while i>2:
        if is_prime(i-2)*is_prime(i):
            print(i,i-2)
            break
        i=i-1
