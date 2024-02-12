#7.8
CarreMagique : List[List[int]]
CarreMagique = [ [2, 7, 6],[9, 5, 1],[4, 3, 8] ]
#q.1

def presence(n:int , l:List[int])->bool:
    i:int
    for i in l:
        if i == n:
            return i == n
    return i == n

#q.2
def mat_presence(n:int , ll:List[List[int]])-> bool:
    i:List[int]
    for i in ll:
        if presence(n , i) == True:
            return True
    return False
    
#q.3
def verif_elems ( n:int , ll:List[List[int]])-> bool:
    m:int
    r:int = 0
    for m in range (1, (n*n)+1):
        if mat_presence(m, ll)== True:
            r = r +1 
    return r == n*n

#q.4
def somme_liste(l:List[int])->int:
    i:int
    r:int = 0
    for i in l:
        r = r + i
    return r

#q.5
def verif_lignes(ll:List[List[int]] , s:int)->bool:
    i:List[int]
    for i in ll:
        if somme_liste(i) != s:
            return False
    return True
    
#q.6
def colonne( j:int , ll:List[List[int]]) -> List[int]:
    i:List[int]
    lr:List[int] = []
    for i in ll:
        lr.append(i[j])
    return lr

#q.7
def verif_colonnes( s:int , mat:List[List[int]])->bool:
    b:int
    for b in range(0,len(mat)-1):
        if somme_liste(colonne(b, mat)) != s:
            return False
    return True
    
#q.8
def diago_1(ll:List[List[int]]) -> List[int]:
    i:List[int]
    lr:List[int] = []
    n:int =0
    for i in ll:
        lr.append(i[n])
        n = n +1
    return lr
def diago_2(ll:List[List[int]]) -> List[int]:
    i:List[int]
    lr:List[int] = []
    n:int =-1
    for i in ll:
        lr.append(i[n])
        n = n - 1
    return lr

#q.9
def verif_magique(ll:List[List[int]]) -> bool:
     i:int
     for i in range (0, len(ll)-1):
         if somme_liste(colonne(i, ll)) == somme_liste(ll[i]) \
            and somme_liste(diago_1(ll)) == somme_liste(diago_2(ll)) \
            and somme_liste(diago_1(ll)) == somme_liste(colonne( i , ll)):
             return True
     return False
