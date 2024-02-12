#Ex 5.1 5.2 5.3 5.4

#Sur cahier

#Ex 5.5

#Q.1
def est_voyelle(c : str)->bool:
    """Précondition : len(c) == 1Retourne True si et seulement si c est une voyelleminiscule ou majuscule."""
    return(c=='a')or(c=='A')\
         or(c=='e')or(c=='E')\
         or(c=='i')or(c=='I')\
         or(c=='o')or(c=='O')\
         or(c=='u')or(c=='U')\
         or(c=='y')or(c=='Y')\
         or(c=='é')or(c=='è')

assert est_voyelle('a')==True
assert est_voyelle('E')==True
assert est_voyelle('b')==False
assert est_voyelle('y')==True
assert est_voyelle('z')==False

#Q.2

def nb_voyelles(s:str)->int:
    """la fonction retourne le nombres de voyelles dans une chaine de caractère"""
    c : str
    voy:int = 0
    for c in s:
        if est_voyelle(c)==True:
            voy = voy +1
    return voy
assert nb_voyelles("AAAAA") == 5
assert nb_voyelles("Ceci est un test") == 5
assert nb_voyelles("la maman du bébé le réconforte")== 11

#Q.3

def sans_voyelles(s : str)->str:
    """ la fct renvoie une chaine de caractere sans voyelle"""
    r : str=''
    d : str
    for d in s:
        if est_voyelle(d)==False:
            r=r+d
    return r

assert sans_voyelles('les revenantes')=='ls rvnnts'
assert sans_voyelles('la disparition')=='l dsprtn'
assert sans_voyelles('')==''   
      
#Q.4
def mot_mystere(s : str)->str:
    """ la fct renvoie un mot mystere en change """
    r : str=''
    e : str
    a:str='_'
    for e in s:
        if est_voyelle(e)==False:
            r=r+e
        else:
                r=r+a
    return r
assert mot_mystere('ceci est un code tres secret')=='c_c_ _st _n c_d_ tr_s s_cr_t'
assert mot_mystere('ceci nest pas un tres bon code secret')=='c_c_ n_st p_s _n tr_s b_n c_d_ s_cr_t'


def est_chiffre(c : str)->bool:
    """Précondition : len(c) == 1 Retourne True si et seulement si c est un chiffre."""
    return('0'<=c)and(c<='9')
assert est_chiffre('4')==True
assert est_chiffre('9')==True
assert est_chiffre('x')==False

#Ex 5.6

#Q.1

def base_comp(c:str)->str:
    """Pré: len(c)==1"""
    if c == 'A':
        return 'T'
    elif c == 'G':
        return 'C'
    elif c == 'T':
        return 'A'
    elif c == 'C':
        return 'G'
    
#Q.2
    
def brin_comp(s:str)->str:
    """"""
    c:str
    r:str=""
    for c in s:
        r = r + base_comp(c)
    return r

#Q.3

def test_comp(s1:str, s2:str)->bool:
    """Pré len(s1) == len(s2)"""
    return brin_comp(s2)== s1

#Q.4

#def test_sous_sequence(b1:str,b2:str)->bool:


#Ex 5.7

#Q.1

def chiffre(c:str)->int:
    return ord(c)-ord('0')

#Q.2

def entier(s:str)->int:
    c:str
    r:int = 0
    i:int
    for i in range(len(s)):
        c = s[i]
        r = r + (chiffre(c))*10**(len(s)-1-i)
    return r

#Q.3

def caractere(n:int)->str:
    return chr(n + ord('0'))

#Q.4

def chaine(n:int)->str:
    i:int=0
    r:str=''
    while i<n:
        r= r + caractere(i)
        i= i+1
    return r
        

#Ex 5.8

#Q.1

def decompression(s : str)->str:
    """Précondition : len(c) == 1 Retourne le nombre d'occurrences du caractère c dans la chaîne s"""
    r:str=''
    d : int
    for d in range(0,len(s)):
        if est_chiffre(s[d])==True:
            r = r + s[d+1]*int(s[d])           
        else:
            r=r+s[d]
    return r
#assert decompression('ab3cd')=='abcccd'

#Q.2

def compression(c:str)->str:
    """ eefzrf"""
    i:str
    l:str = ''
    l2:str = ''
    s:int = 0
    for i in c:
        if i == l2:
            s = s+1
        elif s>1:
            l = l + str(s)
            l = l+ l2
    return l
            


            
            
        
        
            
    
    
