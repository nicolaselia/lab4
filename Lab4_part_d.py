#=David Monge
#AlphaOne
#Lab4
#Part D Fibonnaci Sum 

def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

nNum = 10
for i in range(nNum):
    print(fibo(i))