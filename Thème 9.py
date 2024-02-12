#Theme 9
from typing import Dict, Set
#Ex 9.1
def diff_sym(ens1:Set[K] , ens2:Set[K])-> Set[K]:
    e1:K
    e2:K
    er:Set[K] = set()
    for e1 in ens1:
        if e1 not in ens2:
            er.add(e1)
    for e2 in ens2:
        if e2 not in ens1:
            er.add(e2)
    return er

def diff_sym_opt(ens1:Set[K] , ens2:Set[K])-> Set[K]:
    return {e1 for e1 in ens1 if e1 not in ens2}|{e2 for e2 in ens2 if e2 not in ens1}

def diff_sym2(ens1:Set[K] , ens2:Set[K])-> Set[K]:
    return (ens1|ens2)-(ens1& ens2) 

#Ex 9.2

def repetes(l:List[T]) -> Set[T]:
    e:T
    rep:Set[T] = set()
    ens:Set[T] = set()
    for e in l:
        if e in ens:
            rep.add(e)
        else:
            ens.add(e)
    return rep

def sans_repetes(l:List[T]) -> List[T]:
    vus:Set[T] = set()
    lr:List[T] = []
    i:T
    for i in l:
        if i not in vus:
            vus.add(i)
            lr.append(i)
    return lr

def uniques(l:List[T]) -> Set[T]:
    lr:List[T] = []
    i:T
    unefois:Set[T]= set()
    trop:Set[T] = set()
    for i in l:
        if i in unefois:
            trop.add(i)
        else:
            unefois.add(i)
    return unefois - trop
    
#Ex 9.3
Recette = Dict[str,Set[str]]
Dessert : Recette
Dessert = {
'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'}
,'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'}
,'crepes' : {'oeuf', 'farine', 'lait'}
,'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'}
,'kouign amann' : {'farine', 'beurre', 'sucre'}
}

def nb_ingredients(des:Recette,r:str)->int:
    return len(des[r])

def recette_avec(des:Recette, i:str)->Set[str]:
    oui:Set[str] = set()
    r:str
    e:str
    for r in des:
        for e in des[r]:
            if e == i:
                oui.add(r)
    return oui

def recette_avec_opt(des:Recette, i:str)->Set[str]:
    return {r for r in des for e in des[r] if e==i}      

def tous_ingredients(des:Recette)->Set[str]:
    ingre:Set[str]= set()
    r:str
    e:str
    for r in des:
        for e in des[r]:
            ingre.add(e)
    return ingre

def tous_ingredients_opt(des:Recette)->Set[str]:
    return {e for r in des for e in des[r]}

def table_ingredients(des:Recette)-> Dict[str,Set[str]]:
    ingre:Set[str] = tous_ingredients(des)
    table:Dict[str,Set[str]] = dict()
    e:str
    for e in ingre:
        table[e] = recette_avec(des,e)
    return table

def table_ingredients_opt(des:Recette)-> Dict[str,Set[str]]:
    return {e:recette_avec(des,e) for e in tous_ingredients(des)}

def ingredient_principal(des:Recette)-> str:
    ingre:Set[str] = tous_ingredients(des)
    e:str
    n:int =0
    temp:int = 0
    ilpt:str = ''
    for e in ingre:
        r:str
        for r in des:
            e2:str
            for e2 in des[r]:
                if e2 == e:
                    n = n +1
            if temp < n:
                ilpt = e
        temp:int = n
        n = 0
    return ilpt

def ingredient_principal2(des:Recette)-> str:
    table:Dict[str , Set[str]] = table_ingredients(des)
    i:str
    temp:int = 0
    iplt:str =''
    for i in table:
        n:int = len(table[i])
        if n > temp:
            iplt = i
            temp = n
    return iplt

def recettes_sans(des:Recette, i:str)-> Dict[str,Set[str]]:
    r:str
    dres:Recette = dict()
    for r in des:
        if i not in des[r]:
            dres[r] = des[r]
    return des

def recettes_sans_opt(des:Recette, i:str)-> Dict[str,Set[str]]:
    return {r:des[r] for r in des if i not in des[r]}

#9.4

def est_lettre(c : str) -> bool:
    """Précondition : len(c) == 1 (caractère)
    Retourne True si le caractère c est une lettre,ou False sinon."""
    return ((c >= 'a') and (c <= 'z')) \
    or ((c >= 'A') and (c <= 'Z')) \
    or (c in {'é', 'è', 'à', 'ù', 'oe'})

def frequences_lettres(s:str)->Dict[str,int]:
    c:str
    fl:Dict[str,int] = dict()
    for c in s:
        if est_lettre(c)== True:
            if c in fl:
                fl[c] = fl[c] + 1
            elif c not in fl:
                fl[c] = 1
    return fl

def lettre_freq_max(s:str)->str:
    fl:Dict[str,int] = frequences_lettres(s)
    c:str
    cr:str= ''
    temp:int = 0
    for c in fl:
        if fl[c] > temp:    
            cr = c
            temp = fl[c]
    return cr

def lettres_freq_inf(freqs:Dict[str,int], n:int)->Set[str]:
    c:str
    er:Set[str]= set()
    for c in freqs:
        if freqs[c]<=n:
            er.add(c)
    return er

def lettres_freq_inf_opt(freqs:Dict[str,int], n:int)->Set[str]:
    return {c for c in freqs if freqs[c]<= n}           


#9.5
Produits = Dict[str,float]
base_prix:Produits ={'Sabre Laser': 229.0,'Mitendo DX': 127.30,'Coussin Linux': 74.50,'Slip Goldorak': 29.90,'Station Nextpresso': 184.60}

def prix_moyen(base:Produits)->float:
    prod:str
    s:float = 0
    n:int = 0
    for prod in base:
        s =  s + base[prod]
        n = n+1
    return s/n

def fourchette_prix(pmin:float , pmax:float , base:Produits)->Set[str]:
    ens:Set[str] = set()
    prod:str
    for prod in base:
        if base[prod]>= pmin and base[prod]<= pmax:
            ens.add(prod)
    return ens

Panier = Dict[str,int]
achat:Panier = {'Sabre Laser': 3,'Coussin Linux': 2,'Slip Goldorak': 1}

def tous_dispo(a:Panier , base:Produits)->bool:
    prod:str
    for prod in a:
        prodd:str
        for prodd in base:
            return prod == prodd
        
def prix_achats(a:Panier , base:Produits)->float:
    prod:str
    s:float = 0
    n:int = 0
    for prod in base:
        prodd:str
        for prodd in a:
            if prod == prodd:
                s = s + base[prod]*a[prodd]
                n = n + a[prodd]
    return s

#Ex 9.6

Dict_Ang_Fra : Dict[str, str]
Dict_Ang_Fra = {'the': 'le', 'cat': 'chat',
'fish': 'poisson', 'catches': 'attrape'}
Dict_Fra_Ita : Dict[str, str]
Dict_Fra_Ita = {'le': 'il', 'chat': 'gatto',
'poisson': 'pesce', 'attrape': 'cattura'}

def trad_mot_a_mot(l:List[str],dico:Dict[str,str])->List[str]:
    lr:List[str]=[]
    c:str
    for c in l:
        lr.append(dico[c])
    return lr

def trad_mot_a_mot_opt(l:List[str],dico:Dict[str,str])->List[str]:
    return [dico[c] for c in l]

def dictionnaire_inverse(dico:Dict[str,str])->Dict[str,str]:
    dicor:Dict[str,str]= dict()
    c:str
    for c in dico:
        dicor[dico[c]] = c
    return dicor

def dictionnaire_inverse_opt(dico:Dict[str,str])->Dict[str,str]:
    return {dico[c]:c for c in dico}
    
def compo_dico(dico1:Dict[str,str], dico2:Dict[str,str])->Dict[str,str]:
    c1:str
    dicor:Dict[str,str] = dict()
    for c1 in dico1:
        c2:str
        for c2 in dico2:
            if dico1[c1] == c2:
                dicor[c1]= dico2[c2]
    return dicor

def compo_dico_opt(dico1:Dict[str,str], dico2:Dict[str,str])->Dict[str,str]:
    return {c1:dico2[c2] for c1 in dico1 for c2 in dico2 if dico1[c1]== c2}
    
#9.7

