import math
#Thème 1
#Ex 1.1
#Q.1
def moyenne_trois_nb(a:float ,b:float,c:float)->float:
    """Précondition : aucune. La fct calcule la moy de 3 nb"""
    return (a+b+c)/3
assert moyenne_trois_nb(3,6,-3)== 2
assert moyenne_trois_nb(-3,0,3)== 0
assert moyenne_trois_nb(1.5 , 2.5 , 1.0)== 5/3
#Q.2
def moyenne_ponderee(a:float ,b:float,c:float, pa:float , pb: float , pc:float)->float:
    """Précondition : aucune. La fct calcule la moy pond de 3 nb"""
    return (a*pa+b*pb+c*pc)/3
assert moyenne_ponderee(1,1,1,1,1,1)== 1
assert moyenne_ponderee(1,2,3,3,2,1)== 10/3

#Ex 1.2
#Q.1
def prix_ttc(ht:float,tva:float) -> float:
    """Précondition: ht et tva positifs. La fct le prix ttc"""
    return ht + ht*(tva/100)
assert prix_ttc(100.0 , 20.0)== 120
assert prix_ttc(100, 0.0)== 100.0
assert prix_ttc(100, 100.0)== 200.0
assert prix_ttc(0, 20.0)== 0.0
assert prix_ttc(200, 5.5)== 211.0
#Q.2

def prix_ht(ttc:float,tva:float) -> float:
    """Précondition: ttc et tva positif. La fct calcule le prix hors taxe"""
    return (ttc /(tva+100))*100
assert prix_ht(120 , 20.0)== 100.0
assert prix_ht(100 ,0.0)== 100
assert prix_ht(200,100.0)== 100
assert prix_ht(0, 20.0)== 0
assert prix_ht(211.0, 5.5)== 200.0

#Ex 1.3

#Q.1

def polynomiale(a:float, b:float, c:float , d:float, x:float) -> float:
    """Précondition: aucune. La fct calcule une polynomiale"""
    return a*(x**3)+b*(x**2)+c*x+d
    # return (((((a*x + b) * x) + c) * x) + d) pour mins de multiplication
assert polynomiale(1,1,1,1,2)== 15
assert polynomiale(1,1,1,1,3)== 40

#Q.2

def polynomiale_carre(a:float , b:float, c:float , x:float) -> float:
    """Précondition:aucune. La fct calcule une polynomiale carré"""
    return a*(x**4)+b*(x**2)+c
    # return ((a*x**2+b)x**2)+c
assert polynomiale_carre(1,1,1,2) == 21
assert polynomiale_carre(1,1,1,3) == 91

#Ex 1.4

#Q.1

def aire_disque(r:float) -> float:
    """Précondition: r positif. La fct calcule l'aire d'un disque"""
    return math.pi*(r**2)
assert aire_disque(1)== math.pi
assert aire_disque(0)== 0
assert aire_disque(10)== math.pi*100

#Q.2

def aire_couronne(r1:float, r2:float) -> float:
    """Précondition: r1=<r2. La fct calcule l'aire compris entre r1 et r2"""
    return (math.pi*((r2)**2))-(math.pi*((r1)**2))
assert aire_couronne(10,10) == 0
assert aire_couronne(1, 5.5) == 91.89158511750145

#Ex 1.5

#Q.1

def fahrenheit_vers_celsius(t:float) -> float:
    """Précondition : aucune. La fct calcule la conversion de farenheit en degrés"""
    return (t-32)*(5/9)
assert fahrenheit_vers_celsius(212)==100.0
assert fahrenheit_vers_celsius(32)==0
assert fahrenheit_vers_celsius(41)==5.0

#Q.2

def celsius_vers_farenheit(t:float)-> float:
    """Précondition : aucune. La fct calcule la conversion de degrés en farenheit"""
    return (t*(9/5))+32
assert celsius_vers_farenheit(100.0)== 212
assert celsius_vers_farenheit(0)== 32
assert celsius_vers_farenheit(5.0)== 41

#Ex 1.6

#Q.1

def fermat(n:int) -> float:
    """Précondition: n positif .La fct calcule le n-ième nb de Fermat"""
    return 2**(2**n) + 1
assert fermat(0)== 3
assert fermat(1)== 5
assert fermat(2)== 17
assert fermat(5)== 4294967297

#Q.2
# Expression: fermat(5)% 641 == 0

#Ex 1.7

#Q.1

def excursion(nb_pers:int)-> int:
    """Précondition: nb_pers > 0 .
    La fct calcule le cout minimum pr l'association d'une excursion pour nb_pers"""
    return 

#Ex 1.8 (Fait sur la zone d'evaluation)

#Ex 1.9
def draw_line(x0 : float, y0 : float , x1 : float, y1 : float, color :str ="black") -> Image:
    x0 = 0
    y0 = 0
    x1 = 1000
    x1 = 1000

def show_image(draw_line: Image) -> None:
