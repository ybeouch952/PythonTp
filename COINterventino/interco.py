def f(x) :
    return x*x
def trapeze(a,b,n):
    p=(b-a)/n
    s=0
    for k in range(n):
        s=s+p*(f(a+k*p)+f(a+(k+1)*p))/2
    return s
print(trapeze(0,1,10))