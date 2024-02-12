#Theme 10
#Ex 10.1
#sur feuille

#Ex 10.2
LivresBD : Dict[str,Tuple[str,int]]
LivresBD = {'Les misérables':('Victor Hugo', 5),
'Le dernier des Mohicans':('James F. Cooper', 0),
'Un animal doué de raison': ('Robert Merle', 6),
'Le grand Meaulnes':('Alain Fournier', 1),
'Notre-dame de Paris':('Victor Hugo', 4),
'Les comtemplations':('Victor Hugo', 0) }

def auteurs(livres:Dict[str,Tuple[str,int]])->Set[str]:
    er:Set[str] = set()
    t:str
    for t in livres:
        (nom, _ ) = livres[t]
        er.add(nom)
    return er

def titres_empruntables(livres:Dict[str,Tuple[str,int]])->Set[str]:
    er:Set[str] = set()
    t:str
    for t in livres:
        (_, nombre) = livres[t]
        if nombre !=0:
            er.add(t)
    return er

def titres_auteur( nom:str , livres:Dict[str,Tuple[str,int]]) ->Set[str]:
    er:Set[str] = set()
    t:str
    for t in livres:
        (auteur,_) = livres[t]
        if nom == auteur:
            er.add(t)
    return er    

#Ex 10.4

def melements_list(l:List[T])->Set[T]:
    return {e for e in l}

def melements_dict(d:Dict[T,V])->Set[T]:
    return {e for e in d}


def mlist_de_mdict(d:Dict[str,int])-> List[str]:
    e:str
    lr:List[str] = []
    for e in d:
            n:int = 0
            while n<d[e]:
                lr.append(e)
                n = n+1
    return lr
        
#Ex 10.5

Grandes_Lignes : Dict[str, Set[str]]
Grandes_Lignes = {'Paris': {'Strasbourg', 'Dijon', 'Toulouse',
'Lille', 'Lyon', 'Bordeaux'},
'Strasbourg':{'Paris', 'Dijon', 'München'},
'München': {'Strasbourg'},
'Dijon': {'Paris', 'Strasbourg', 'Lyon', 'Toulouse'},
'Lyon':{'Paris', 'Dijon', 'Toulouse'},
'Toulouse': {'Paris', 'Lyon', 'Dijon', 'Bordeaux'},
'Bordeaux': {'Nantes', 'Paris'},
'Nantes': {'Paris', 'Bordeaux','Quimper'},
'Quimper':{'Nantes'}, 'Ajaccio': {'Bastia'},
'Bastia': {'Ajaccio'}, 'Lille': {'Paris'}}

def trajet_direct(carte:Dict[str,Set[str]], st1:str,st2:str)->bool:
    if st1 not in carte:
        return False
    return st2 in carte[st1]

def ajout_station(st:str , crpd:Set[str], carte:Dict[str,Set[str]])->Dict[str,Set[str]]:
    carte[st] = crpd
    return carte

Nouvelles_Lignes : Dict[str, Set[str]]
Nouvelles_Lignes = ajout_station('Limoges', {'Paris', 'Toulouse', 'Bordeaux'},
Grandes_Lignes)

def 
