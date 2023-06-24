def is_lower(h):
    for x in range (0,len(h)-1):
        k=ord(h[x])
    if ord("a")<=k<=ord("z"):
        return True
    else:
        return False  


def is_upper(h):
    for x in range (0,len(h)-1):
        k=ord(h[x])
    if ord("A")<=k<=ord("Z"):
        return True
    else:
        return False  


def is_alphanum(h):
    for x in range (0,len(h)-1):
        k=ord(h[x])
    if ((ord("a")<=k<=ord("z")) or (ord("A")<=k<=ord("Z")) or (ord("0")<=k<=ord("9"))):
        return True
    else:
        return False 
    
    
def is_alpha(h):
    for x in range (0,len(h)-1):
        k=ord(h[x])
    if ((ord("a")<=k<=ord("z")) or (ord("A")<=k<=ord("Z"))):
        return True
    else:
        return False  
    
    
def is_digit(h):
    for x in range(0,len(h)-1):
        k=ord(h[x])
    if ord("0")<=k<=ord("9")  :
        return True
    else:
        return False  


def s_upper(st):
    s=""
    for x in st:
        if ord(x)>=97 and ord(x)<=122:
            s+=chr(ord(x)-32)
        else:
            s+=x
    return s


def s_lower(st):
    s=""
    for x in st:
        if ord(x)>=65 and ord(x)<=90:
            s+=chr(ord(x)+32)
        else:
            s+=x
    return s       


    