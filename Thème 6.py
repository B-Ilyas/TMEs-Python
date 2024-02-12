#Theme 6
import math
#Ex 6.1 6.2 6.4

#voir sur cahier

#Ex 6.3

#q.1
def liste_diviseurs(a:int)-> List[int]:
    """Pré : a > 0 , la fonction renvoie une liste de diviseur de a"""
    i:int
    l:List[int]=[]
    for i in range (1,a+1):
        if a%i ==0 :
            l.append(i)
    return l

def liste_diviseurs2(a:int)-> List[int]:
    """Pré : a > 0 , la fonction renvoie une liste de diviseur de a"""
    i:int
    l:List[int]=[]
    return[i for i in range (1,a+1)if a%i ==0]
assert liste_diviseurs(18) == [1,2,3,6,9,18]
assert liste_diviseurs(24) == [1,2,3,4,6,8,12,24]
assert liste_diviseurs(8) == [1,2,4,8] 
assert liste_diviseurs(15) == [1,3,5,15]
assert liste_diviseurs2(18) == [1,2,3,6,9,18]
assert liste_diviseurs2(24) == [1,2,3,4,6,8,12,24]
assert liste_diviseurs2(8) == [1,2,4,8] 
assert liste_diviseurs2(15) == [1,3,5,15]
#Q.2
def liste_diviseurs_impairs(a:int)-> List[int]:
    """Pré : a > 0 , la fonction renvoie une liste de diviseur de a"""
    i:int
    l:List[int]=[]
    for i in range (1,a+1):
        if a%i ==0 :
            k:int
            for k in range (0,i):
                if i == 2*k+1:
                    l.append(i)
                else:
                    k = k+1
    return l

#Ex 6.5

#q.1

def decoupage_simple(l:List[T] ,i:int , j:int)->List[T]:
    """Pré : i<= j. La fct renvoie un decoupage de l a partir de i et j"""
    lr:List[T] = []
    v:int
    for v in range(i,j+1):
        lr.append(lr[v])
    return lr
    
lcomptine : List[str]
lcomptine = ['am', 'stram', 'gram', 'pic', 'pic', 'col', 'gram']
assert decoupage_simple(lcomptine, 1, 3) == lcomptine[1:3]
assert decoupage_simple(lcomptine, 3, 4) == lcomptine[3:4]
assert decoupage_simple(lcomptine, 3, 3) == lcomptine[3:3]
assert decoupage_simple(lcomptine, 5, 3) == lcomptine[5:3]
assert decoupage_simple(lcomptine, 0, 7) == lcomptine[0:7]

def decoupage_pas(l:List[T] ,i:int , j:int , p:int)->List[T]:
    """"""
    lr:List[T] = []
    v:int = i
    while v <= j:
        lr.append(lr[i])
        v = v+p
    return lr

assert decoupage_pas(lcomptine,1, 5, 2) == lcomptine[1:5:2]
assert decoupage_pas(lcomptine,2, 6, 1) == lcomptine[2:6:1]

#q3
def decoupage_pas_inv(l:List[T] ,i:int , j:int , p:int)->List[T]:
    """"""
    lr:List[T] = []
    v:int = j
    while v >= i:
        lr.append(lr[v])
        v = v+p
    return lr

assert decoupage_pas_inv(lcomptine, 5, 2, -2) == lcomptine[5:2:-2]
assert decoupage_pas_inv(lcomptine, 6, 0, -1) == lcomptine[6:0:-1]
assert decoupage_pas_inv(lcomptine, 6, 0, -3) == lcomptine[6:0:-3]

def normalisation(i : int, long: int) -> int:
    """Précondition: long >= 0 Retourne la normalisation de l'indice k pour une liste de longueur long."""
    if i < 0: # indice négatif
        if -i <= long: # dans l'intervalle [O;long]
            return long + i
        else: # en dehors de l'intervalle [0;long]
            return 0
    else: # indice positif
        if i > long: # en dehors de l'intervalle [0;long]
            return long
        else:
            return i # déjà normalisé

#Ex 6.6

def somme (n:List[float])-> float:
    """la fct calcule la somme des valeurs de liste"""
    s:float=0
    i:float
    for i in n:
        s = s + i
    return s
        
assert somme([1,2,3,4,5]) == 15
assert somme([1,2.5,3.2,4,5]) == 15.7
assert somme([1, 2.5 , 3.5 , 4 , 5]) == 16.0
assert somme([]) == 0

def moyenne (n:List[float]) -> float:
    """la fct calcule la moyenne des valeurs d'une liste"""
    s:float=0
    i:float
    for i in n:
        s= (somme(n))/(len(n))
    return s

assert moyenne([1,2,3,4,5]) == 3.0
assert moyenne([1, 2.5 , 3.5 , 4 , 5]) == 3.2
assert moyenne([5]) == 5.0

def carres (L:List[float])->List[float]:
    """la fct calcule les carrés de chaque valeurs"""
    r:List[float] = []
    i:float
    for i in L:
        r.append(i**2)
    return r

le:List[int] = [1,2,3,4,5,6,7,8,9]

def cproc(l:List[float])->None:
    """***Procedure***la fct calcule les carrés de chaque valeurs"""
    i:float
    for i in l:
        l.append(i**2)
        
assert cproc(le) == None
assert le == [1,4,9,16,25,36,49,64,81]

assert carres([1,2,3,4,5])== [1,4,9,16,25]
assert carres([1,-2,-3,4,5])==[1,4,9,16,25]
assert carres([])==[]
assert carres([10, 0.5 , 2.0])== [100 , 0.25 , 4.0]

def variance (n:List[float]) -> float:
    """" la fct calcule la variance da la liste n """
    return moyenne(carres(n)) - (moyenne(n))**2

assert variance ([10,10,10,10])== 0.0
assert variance ([20,0,20,0])== 100.0

def ecart_type(n:List[float]) -> float:
    """la fct calcule l'ecart type"""
    return math.sqrt(variance(n))

assert ecart_type([10,10,10,10])== 0.0
assert ecart_type([20,0,20,0])== 10.0
assert ecart_type([15,15,5,5])== 5.0
assert ecart_type([12,11,10,12,11])== 0.7483314773547993

#Ex 6.7

def liste_mult(n:List[float] , m:float)-> List[float]:
    """ la fct retourne une liste de valeur multiplié par m"""
    r:float
    l:List[float]=[]
    for r in n:
        l.append(r*m)
    return l

def lm_proc(l:List[float] , m:float)->None:
    """***Procedure*** la fct retourne une liste de valeur multiplié par m"""
    r:float
    for r in l:
        l.append(r*m)

assert lm_proc(le,2) == None
assert le == [2,4,6,8,10,12,14,16,18]

assert liste_mult([3,5,9,4],2)== [6,10,18,8]
assert liste_mult([],2)== []

def liste_div(n:List[int],m:int)-> List[float]:
    """Pré : m !=0
        la fct retourne une liste de valeur divisé par m"""
    r:int
    l:List[float]=[]
    for r in n:
        if r%m == 0:
            l.append(r/m)
    return l

def ld_proc(l:List[int],m:int)->None:
    """***Procedure*** Pré : m !=0
        la fct retourne une liste de valeur divisé par m"""
    r:int
    for r in l:
        if r%m == 0.0:
            l.append(r/m)

assert ld_proc(le, 2) == None
assert le == [0.0,1.0,2.0,3.0,4.0]

assert liste_div([2,7,9,24,6],2)== [1.0,12.0,3.0]
assert liste_div([2,7,9,24,6],3)== [3.0,8.0,2.0]
assert liste_div([2,7,9,24,6],5)== []
assert liste_div([2,7,9,-24,6],-3)== [-3,8,-2]
assert liste_div([], 3) == []

#Ex 6.9

def jonction(l : List[str], c : str)->str:
    """Précondition : len(c) = 1 Retourne la chaîne composée de la jonction deschaîne de L séparées deux-à-deux par lecaractère séparateur c."""
    r:str
    s:str= ''
    for r in l:
        s = s + r + c 
    return s

assert jonction(['a','b','c','d'],'.') == 'a.b.c.d.'
assert jonction(['les', 'mots','de','cette','phrase'],' ') == 'les mots de cette phrase '

def separation(s:str , c:str) -> List[str]:
    """"""
    r:str
    i:int = 0
    lr:List[str]=[]
    j:int =0
    for r in s:
        if r == c:
            lr.append(s[j:i+1])
            j = i
        i = i+1
    return lr
