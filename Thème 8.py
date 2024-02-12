#Theme 8
#8.2

#q.1

def alphabet()-> List[str]:
    return [chr(i) for i in range (97 , 123)]
assert alphabet() == ['a','b','c','d','e','f','g','h','i','j','k','l','m',\
'n','o','p','q','r','s','t','u','v','w','x','y','z']
#q.2
def voyelle(c:str)->bool:
    """len(c) == 1"""
    return c == 'a' or c == 'e' or c =='i' or c=='y' or c=='o' or c=='u'

#q.3
def voy_alpha()->List[str]:
    return [c for c in alphabet() if voyelle(c)==True]
#q.4
def consonne() ->List[str]:
    return [c for c in alphabet() if voyelle(c)==False]

#8.3

#q.1
def liste_non_multiple(n:int , l :List[int])->List[int]:
    return [i for i in l if n%i != 0]

#q.2
def eratosthene(n:int)->List[int]:
    lr:List[int] = []
    lr:List[int] = lr[2:n+1:1]
    i:int
    for i in range (2,n+1):
        lr = liste_non_multiple(i , lr[i:n:1])
    return lr
    


#8.4
#q.1
def moyenne(l:List[int])-> float:
    """"""
    i:int
    s:int=0
    n:int=0
    for i in l:
        s = s + i
        n = n+1
    return s/n

#q.2
def ecart_nombre(l:List[int], x:int)->List[float]:
    return [abs(x-i) for i in l]

#q.3
def liste_carre(l:List[int])-> List[int]:
    return [i*i for i in l]
#q.4
def variance(l:List[int])-> float:
    i:int
    m:float = moyenne(l)
    v:float=0
    n:int =0
    for i in l:
        v = v + abs((i - m)**2)
        n = n +1
    return v/n

#8.5
#q.1
def liste_caracteres(c:str)->List[str]:
    return [s for s in c]

#q.2
def chaine_de(l:List[str])-> str:
    s:str
    cr:str=''
    for s in l:
        cr= cr +s
    return cr
        
#q.3
def num_car (c:str)->int:
    return ord(c) - 97

#q.4
def car_num(n:int)->str:
    return chr(n+97)

#q.5
def rot13(c:str)-> str:
    if num_car(c) >=13 and num_car(c)<= 25 :
        return car_num((num_car(c) + 13)% 26)
    elif num_car(c) >= 0 and num_car(c) < 13:
        return car_num( num_car(c) + 13)
    else:
        return c


#q.6
def codage_rot13(c:str)->str:
    lr:List[str] = [rot13(s) for s in c]
    l:str
    lf:str =''
    for l in lr:
        lf = lf + l
    return lf

#8.6


