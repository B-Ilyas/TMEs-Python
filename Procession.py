def u (n:int) -> float:
    if n == 0:
        return 2
    else:
        return 5*u(n-1) + 4

def u2 (n:int)->float:
    if n ==0:
        return 0
    else:
        return 1/(2- u2(n-1))
    
