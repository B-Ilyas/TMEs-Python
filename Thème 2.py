
import math

#Ex 2.1

#Reponse sur feuille

#Ex 2.2

def mention(n:int)-> str:
    """Pré : n>0 . La fct attribue la mention depuis la note"""
    if n >= 16:
        return 'TB'
    elif n >= 14:
        return 'B'
    elif n >= 12:
        return 'AB'
    elif n >= 10:
        return 'Passable'
    else:
        return 'Sakujo'

assert mention(16)== 'TB'
assert mention(8)== 'Sakujo'
#Ex 2.3

#Q.1

def f(n1 : float, n2 : float, n3 : float) -> str:
    """Précondition : n1 ! = n2 and n2 ! = n3 and n3 ! = n1
    retourne un cas parmi 6 selon les valeurs de n1, n2 et n3."""
    if n1 < n2 and n2 < n3:
        return 'cas 1'
    elif n1 < n3 and n3 < n2:
        return 'cas 2'
    elif n2 < n1 and n1 < n3:
        return 'cas 3'
    elif n2 < n3 and n3 < n1:
        return 'cas 4'
    elif n3 < n1 and n1 < n2:
        return 'cas 5'
    else:
        return 'cas 6'

assert f(1,2,3)=='cas 1'
assert f(1,3,2)=='cas 2'
assert f(2,1,3)=='cas 3'
assert f(3,1,2)=='cas 4'
assert f(2,3,1)=='cas 5'
assert f(1,1,1)=='cas 6'

#Q.2

def f2(n1 : float, n2 : float, n3 : float) -> str:
    """Précondition : n1 != n2 and n2 != n3 and n3 != n1
    retourne un cas parmi 6 selon les valeurs de n1, n2 et n3."""
    if n1 < n2 :
        if n2 < n3:
            return 'cas 1'
        elif n3 < n1:
            return 'cas 5'
    elif n1 < n3:
        if n3 < n2:
            return 'cas 2'
        elif n2 < n1:
            return 'cas 3'
    elif n3 < n1:
        if n1 < n2:
            return 'cas 5'
        elif  n2 < n3:
            return 'cas 4' 
    else:
        return 'cas 6'

assert f2(1,2,3)=='cas 1'
assert f2(1,3,2)=='cas 2'
assert f2(2,1,3)=='cas 3'
assert f2(3,1,2)=='cas 4'
assert f2(2,3,1)=='cas 5'
assert f2(1,1,1)=='cas 6'

#Ex 2.4

#Q.1

def egal_eps(x1:float, x2:float, epsilon:float)->bool:
    """Précondition: epsilon>0. La fct test une egalité à epsilon près"""
    return abs(x1-x2)<=epsilon
    
assert egal_eps(2.13,2,0.13)== True
assert egal_eps(-1,1,0.1)== False
assert egal_eps(-1,-1,0.1)== False

#Q.2

def fiabilite(v1:float, v2:float,v3:float, epsilon:float)->str:
    """Précondition: epsilon>0. La fct test une egalité à epsilon près"""
    if abs(v1-v2)<=epsilon:
        if abs(v2-v3)<=epsilon:
            if abs(v1-v3)<=epsilon:
                return "Taux de fiabilité : 1"
            else :
                return "Taux de fiabilité : 2/3" 
        elif abs(v1-v3)<=epsilon:
            return "Taux de fiabilité : 2/3"
    elif abs(v2-v3)<=epsilon:
        if abs(v1-v3)<=epsilon:
            return "Taux de fiabilité : 2/3"
        else:
            return "Taux de fiabilité : 0"
    else:
        return "Taux de fiabilité : 0"

assert fiabilite(3,3,3,1.1) == "Taux de fiabilité : 1"
assert fiabilite(3,2,1,1.1) == "Taux de fiabilité : 2/3"
assert fiabilite(1,2,3,1.1) == "Taux de fiabilité : 2/3"
assert fiabilite(1,3,2,1.1) == "Taux de fiabilité : 2/3"
assert fiabilite(1,3,5,1.1) == "Taux de fiabilité : 0"
assert fiabilite(1,2,5,1.1) == "Taux de fiabilité : 0"
assert fiabilite(1,5,2,1.1) == "Taux de fiabilité : 0"
assert fiabilite(5,1,2,1.1) == "Taux de fiabilité : 0"
        
#Ex 2.5

#Q.1

def volume_tetraedre(a:float,b:float,c:float,d:float,e:float,f:float)-> float:
    """Précondition: a, b ,c ,d,e,f positifs. La fct calcule le volume d'un tetraedre"""
    x:float
    y:float
    z:float
    p:float
    q:float
    r:float
    
    x = (a**2) + (b**2) - (d**2)
    y = (b**2) + (c**2) - (e**2)
    z = (a**2) + (c**2) - (f**2)
    p= 4*(a**2)*(b**2)*(c**2)
    q= (a**2)*(y**2) + (b**2)*(z**2) + (c**2)*(x**2)
    r= x*y*z
    
    return (1/12)* math.sqrt(p-q+r)
assert volume_tetraedre(1, 1, 1, 1, 1, 1)== 0.11785113019775792
assert volume_tetraedre(2, 2, 2, 2, 2, 2)== 0.9428090415820634

#Q.2

def volume_tetraedre_regulier(a:float) -> float:
    """Précondition: a positifs. La fct calcule le volume d'un tetraedre"""
    p:float
    q:float
    r:float
    p= 4*(a**6)
    q= (a**6) + (a**6) + (a**6)
    r= a**6
    
    return (1/12)* math.sqrt(p-q+r)
assert volume_tetraedre_regulier(1)== 0.11785113019775792
assert volume_tetraedre_regulier(2)== 0.9428090415820634

#Ex 2.6

#Q.1

def ou(p : bool, q : bool) -> bool:
    """Retourne la disjonction de p et q."""
    if p == True:
         if q == True:
            return True
         else:
            return True
    else:
        return False
assert ou(True, True)== True
assert ou(True, False)== True
assert ou(False, True)== True
assert ou(False,False)== False

def et(p : bool, q : bool) -> bool:
    """Retourne la conjonction de p et q."""
    if p == True:
         if q == True:
            return True
         else:
            return False
    if q == True:
         if p == True:
            return True
         else:
            return False
    else:
        return False 

assert et(True, True)== True
assert et(True, False)== False
assert et(False, True)== False
assert et(False,False)== False

def non(p : bool) -> bool:
    """Retourne la négation de p."""
    if p == True:
        return False
    else:
        return True
assert non(True)== False
assert non(False)== True
        
assert ou(et(True, False), False)== False
assert et(ou(False, True), non(False))== True
assert non(non(3 == 1 + 2))== True

assert ou(3 == 3, 5 // 0 == 2)== True
assert et(3 == 3, 5 // 0 == 2)== False

#Q.3

def implique(p : bool, q : bool) -> bool:
    """Retourne le résultat de 'p implique q'."""
    if non(p)== True:
        if q == True:
            return True
        else:
            return False
    elif non(p)== False:
        if q == False:
            return True
        else:
            return False
assert implique(False, False)== True
assert implique(True, False) == False
assert implique(True, 3 == 3)== True

def ou_exclusif(p : bool, q : bool) -> bool:
    """Retourne le résultat de 'p xor q'."""
    if p == True:
        if non(q) == False:
            return True
        else:
            return False
    elif non(p) == False:
        if q == True:
            return True
        else:
            return False

assert ou_exclusif(True, False)==True
assert ou_exclusif(3 == 2, 3 == 3)==True
assert ou_exclusif(2 == 2, 3 == 3)==False
assert ou_exclusif(2 == 1, 3 == 1)==False

#Q.4

def equivalent(p : bool, q : bool) -> bool:
    """Retourne True si et seulement si p et q sont équivalents."""
    if implique(p,q)== True:
        if implique(q,p)==True:
            return True
        else:
            return False
    elif implique(p,q)==False:
        if implique(q,p)==False:
            return True
        else:
            return False
        
assert equivalent(True, 3 == 3)== True
assert equivalent(True, 3 == 4)== False
assert equivalent(3 == 2, 3 == 8)==True
assert equivalent(3 == 3, 3 == 8)== False

#Ex 2.7

#Q.1




    
