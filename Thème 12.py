#Theme 12
#Ex 12.1

def censurer(l:List[str] , e:Set[str])-> None:
    s:int
    for s in range(len(l)):
        if l[s] in e:
            l.append = "***CENSURE***"

t0:List[str]= ['le', '***CENSURE***', 'est', 'un','***CENSURE***', 'pour', "l'", 'homme']

#exercice 12.2

def  inverser(l : List[T])->None:
    """***Procédure***Renverse la liste l en place."""
    k:int
    for k in range(0, len(l)//2):
        temp : T=l[k]
        l[k]=l[len(l)-k-1]
        l[len(l)-k-1]=temp
        
# Jeux de tests
l0 : List[int]=[1, 2, 3]
assert inverser(l0)==None
assert l0==[3, 2, 1]

#q.1
Matrice=List[List[int]]
def inverser_lignes(m:Matrice)->Matrice:
    inverser(m)
    return m

#q.2
def inverser_colonnes(m:Matrice)->Matrice:
    i:List[int]
    for i in m:
        inverser(i)
    return m

#q.3
def demitour(m:Matrice) -> Matrice:
    inverser_lignes(m)
    inverser_colonnes(m)
    return m
m3 :Matrice = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

#12.4

def trier_bulles(l:List[T]) -> None:
    """***Procédure***"""
    i:int
    j:int
    temp:T
    for i in range (len(l)-1):
        for j in range(len(l)-i-2):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp


l1 : List[int]=[1, 0, 0, 1, 0, 1, 1]


def trier_bulles_optim(l:List[T]) -> None:
    """***Procédure***"""
    i:int
    j:int
    temp:T
    lr:List[T] = []
    n:int = 0
    for i in range (len(l)-1):
        n:int = 0
        for j in range(len(l)-i-2):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                n = n +1
            elif n == 0:
                pass
