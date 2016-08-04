def pow(x,y):
    if(y==0): 
        return 1
    if(y==1): 
        return x
    if(y<0): 
        return 1/pow(x,abs(y))
    if(y%2==0):
        r = pow(x,y/2)
        return r*r
    else :
        r = pow(x,(y-1)/2)
        return r*r*x    
print(pow(3,-3))
