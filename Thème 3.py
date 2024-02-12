import math
import random
#Ex 3.1

#Q.1

def somme_impairs_inf(n:int)->int:
    """Préconditions: n>0. La fct calcule la somme des entieres impairs inferieurs ou egaux à n"""
    s:int =0
    i:int=1
    while i<=n:
        s = s+i
        i = i+2
    return s
assert somme_impairs_inf(0) == 0
assert somme_impairs_inf(1) == 1
assert somme_impairs_inf(2) == 1
assert somme_impairs_inf(3) == 4
assert somme_impairs_inf(4) == 4
assert somme_impairs_inf(5) == 9
assert somme_impairs_inf(8) == 16

#Q.2

def somme_premiers_impairs(n:int)->int:
    """Préconditions: n>0. La fct calcule la somme des premiers entiers impairs """
    s:int = 0
    i:int = 1
    while i<=n:
        s = i**2
        i = i+1
    return s

assert somme_premiers_impairs(1)== 1
assert somme_premiers_impairs(2)== 4
assert somme_premiers_impairs(3)== 9
        
#Q.3
#Reponse sur feuille

#Ex 3.2
#Reponse sur cahier

#Ex 3.3

#Q.1

def divise(n:int , p:int)->bool:
    """Pré n>0 p>0"""
    return p%n==0
assert divise(1,4)== True
assert divise(2,4)== True
assert divise(3,4)== False
assert divise(4,2)== False

#Q.2
def est_premier(n:int) ->bool:
    """Préc n>=0. La fct calcule si n est premier"""
    if n<=1:
        return False
    i:int = 2
    while i< n:
        if divise(i,n):
            return False
        i=i+1
    return True
assert est_premier(9)== False
assert est_premier(3)== True        
assert est_premier(7)== True

#Ex 3.4

#Q.1

def reste(a:int , b:int)-> int:
    """Pré:a>=0 b>0. La fct renvoie le reste de la div euclidienne"""
    r:int = a
    while r>=b:
        r = r-b
    return r
                
#Q.2

def est_divisible(a:int,b:int) ->bool:
    return reste(a,b)==0

#Q.3
def ppcm(a:int,b:int) -> int:
    if est_divisible(a,b) == False:
        return a*b
    else:
        q : int = a
        r : int = b
        temp : int = 0
        while r != 0:
            temp = q % r
            q = r
            r = temp
        return q
        
        
#Ex 3.5

#Q.1
    
def fibonacci(n:int)->int:
    """Pré: n>=0"""
    f0:int=0
    f1:int=1
    if n==0:
        return f0
    elif n==1:
        return f1
    else:
        fn:int
        i:int=2
        while i<=n:
            fn=f0+f1
            f0=f1
            f1=fn
            i=i+1
        return f1

#Q.2

#voir sur cahier

#Q.3
    
def fibo_diff(k:int)->float:
    """Pré: k>=2"""
    return fibonacci(k)/fibonacci(k-1)

#Q.4

def fibo_approx(n:int)->float:
    return (((1 + math.sqrt(5))/2)**n)/(math.sqrt(5))

#Ex 3.6

#Q.1

def partie_entiere(x:float)->int:
    n:int=0
    d:float= x
    while n<=x:
        if x<n+1:
            d = n
        n=n+1
    return d

#Q.2

def encadrement(x:float,e:float)->int:
    n:int=0
    d:float= x
    while n<=x:
        if x<n+e:
            d = n
        n=n+1
    return d

#Q.3

def partie_entiere2(x:float)->int:
    e:int=1
    return encadrement(x,e)

#Ex 3.7

#Q.1

def suite_racine(x:int, n:int)->float:
    u:float
    if n==0:
        u=1
    else:
        i:int
        u=1
        for i in range(1,n+1):
            u = (u+(x/u))/2
    return u        

#Q.2
def approx_racine_stable(n:int)->float:
    if n==0:
        u=1
    u:float=1
    u1:float=1
    i:int
    for i in range(1,n+1):
            u = (u+(u1/u))/2
            if u1 == u:
                i = n+1
            u1 = u   
    return u1

#Ex 3.8

#Q.1

def lancer_de6()->float:
    return math.floor(random.random()*6)+1
#Q.2

#q.3

def moyenne_plusieurs_lancers(n:int)->float:
    i:int =0
    s:float =0
    while i < n+1:
        s = s + math.floor(random.random()*6)+1
        i = i+1
    return s/n

#q.4
def freq(n:int , r:int)->float:
    i:int =0
    s:float =0
    f:int = 0
    while i < n+1:
        s = math.floor(random.random()*6)+1
        if s == r:
            f = f+1
        i = i+1
    return f/n

#q.5
def lancer_deN(n:int)->float:
    return math.floor(random.random()*n)+1
