def reverse(text: str) -> str:
    
    return text[::-1]
    pass

def first_to_upper(text: str) -> str:
    L=text.split()
    M=[]
    for i in L:
        M.append(i[0].capitalize()+i[1:])
    r =" ".join(M)
    return r
    pass

def count_vowels(text: str) -> int:

    vowels = ['a','A','e','E','i','I','o','O','u','U','y','Y']
    total = 0
    for s in text:
        if s in vowels:
            total += 1

    return total
    pass


def sum_digits(text: str) -> int:
    L=list(text)
    c=0
    for i in L:
        if(i=="9" or i=="8" or i=="7" or i=="6" or i=="5" or i=="4" or i=="3" or i=="2" or i=="1" or i=="0"):
             c+=int(i)
    return c
    pass


def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parametrs
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    ""
    pass
