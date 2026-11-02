def plus_petit_diviseur(n):
    """
    L'entier n étant supérieur ou égal à 2 cette fonction renvoie le plus 
    petit diviseur de n qui soit strictement plus grand que 1.
    (Si ce diviseur est égal à n c'est que n est premier.)
    """
    k = 2
    while k * k <= n:
        if (n % k) == 0:
            return k
        k += 1
    return n


def valuation(p, n):
    """
    L'entier p étant un diviseur premier de n, cette fonction renvoie 
    l'exposant k maximal tel que p^k divise n. Il s'agit donc de la
    valuation p-adique de n.
    """
    k = 0
    while (n % p**k) == 0:
        k += 1
    return k-1


def decomposition(n):
    """
    L'entier n est supposé supérieur ou égal à 2. Cette fonction renvoie
    la décomposition de n en facteur premier sous la forme 
    [(p1, a1), ..., (pk, ak)] où p1 < p2 < ... < pk sont les facteurs premiers
    de n et a1, a2, ..., ak sont les valuations correspondantes.
    """
    RES = []
    m = n # une copie
    while m != 1:
        p = plus_petit_diviseur(m)
        a = valuation(p, m)
        m = m//(p**a)
        RES.append((p, a))
    return RES


#print(decomposition(90))