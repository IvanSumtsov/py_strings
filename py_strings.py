def reverse(text: str) -> str: 
    return text[::-1]

def first_to_upper(text: str) -> str:
    new_str=""

    first_letter=True
    for c in texdt:
        if c in string.whitespace or c in string.punktuation:
            new_str+=c
            first_letter=True
            continue
        if c in string.digits:
            new_str+=c
            first letter =False
            continue
        if c.islower() and first_letter:
            new_str+=c.upper()
            first_letter=False
            continue
        new_str+=c
        first_letter=False
    return new_str

def count_vowels(text: str) -> int:
    vowels = ['a','A','e','E','i','I','o','O','u','U','y','Y','ą','Ą','ę','Ę','ó','Ó']
    total = 0
    for s in text:
        if s in vowels:
            total += 1

    return total
    
def sum_digits(text: str) -> int:
    L=list(text)
    c=0
    for i in L:
        if(i=="9" or i=="8" or i=="7" or i=="6" or i=="5" or i=="4" or i=="3" or i=="2" or i=="1" or i=="0"):
             c+=int(i)
    return c
    
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
    """
    pass
