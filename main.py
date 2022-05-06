def Twin_Primes(n,m):
    l=[]
    def prime(n):
        f = 0
        for i in range(2,n//2+1):
            if n%i==0:
                f=1
                break
        return f
                
    for i in range(n,m):
        if i==1:
            continue
        if prime(i)==0 and prime(i+2)==0:
            l.append((i,i+2))
    return l
            
        
            
    
n=int(input("num1 n:"))
m=int(input("num2 m:"))
print("Twin prime are:",sorted(Twin_Primes(n, m)))