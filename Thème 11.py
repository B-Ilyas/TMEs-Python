#Theme 11
#Ex 11.1

#q.1

def fibo(n:int)-> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
#q.3   
def fibofast(n:int , a:int , b:int)->int:
    if n ==0:
        return a
    elif n >0:
        return fibofast(n-1,b,a+b)
#q.5
def fibit(n:int)-> int:
    a:int = 0
    b:int = 1
    i:int = 1
    while i <=n:
        temp:int = b
        b = a + b
        a = temp
        i = i + 1
    return a


#Ex 11.2

#q.1
def puissance (x:int ,n:int) -> int:
    if n == 0:
        return 1
    else:
        return x*puissance(x,n-1)

#q.5
def puissance_rapide(x:int , n :int) -> float:
    if n == 0:
        return 1
    else:
        if n%2 == 0:
            return puissance_rapide(x,n //2) * puissance_rapide(x , n//2)
        elif n%2 == 1:
            return x*puissance_rapide(x,n //2) * puissance_rapide(x , n//2)

#Ex 11.6

#Q.1
def fmap(f : Callable[[T], U], lst : List[T]) -> List[U]:
    v:T
    lr:List[U]=[]
    for v in lst:
        lr.append(f(v))
    return lr

#Q.2
def fmap2(f : Callable[[T], U], lst : List[T]) -> List[U]:
    v:T
    return [f(v)for v in lst]

#Q.3
def ffilter(f : Callable[[T], bool], lst : List[T]) -> List[T]:
    v:T
    lr:List[T]=[]
    for v in lst:
        if f(v) == True:
            lr.append(v)
    return lr

#q.4
def ffilter2(f : Callable[[T], bool], lst : List[T]) -> List[T]:
    v:T
    return [v for v in lst if f(v) == True]

#Ex 11.7
#q.1
def fzip(lst1 : List[T], lst2 : List[U]) -> List[Tuple[T, U]]:
    lr:List[Tuple[T,U]]= []
    i:int
    for i in range(min(len(lst1) , len(lst2))):
        lr.append((lst1[i], lst2[i]))
    return lr

#q.2
def funzip(lst : List[Tuple[T, U]]) -> Tuple[List[T], List[U]]:
    i:Tuple[T,U]
    lt:List[T] = []
    lu:List[U] = []
    for i in lst:
        (info1 , info2) = i
        lt.append(info1)
        lu.append(info2)
    return lt , lu

#q.3
def fzip2(lst1 : List[T], lst2 : List[U] , f:Callable[[T,U],V]) -> List[V]:
    lr:List[V]= []
    i:int
    for i in range(min(len(lst1) , len(lst2))):
        lr.append(f(lst1[i], lst2[i]))
    return lr

