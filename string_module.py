#islower()
def is_lower(h):
    for x in range (0,len(h)-1):
        k=ord(h[x])
    if ord("a")<=k<=ord("z"):
        return True
    else:
        return False  

#isupper()
def is_upper(h):
    for x in range (0,len(h)-1):
        k=ord(h[x])
    if ord("A")<=k<=ord("Z"):
        return True
    else:
        return False  

#isalphanum()
def is_alphanum(h):
    for x in range (0,len(h)-1):
        k=ord(h[x])
    if ((ord("a")<=k<=ord("z")) or (ord("A")<=k<=ord("Z")) or (ord("0")<=k<=ord("9"))):
        return True
    else:
        return False 
    
#isalpha()    
def is_alpha(h):
    for x in range (0,len(h)-1):
        k=ord(h[x])
    if ((ord("a")<=k<=ord("z")) or (ord("A")<=k<=ord("Z"))):
        return True
    else:
        return False  
    
#isdigit()    
def is_digit(h):
    for x in range(0,len(h)-1):
        k=ord(h[x])
    if ord("0")<=k<=ord("9")  :
        return True
    else:
        return False  


#upper()    
def s_upper(st):
    s=""
    for x in st:
        if ord(x)>=97 and ord(x)<=122:
            s+=chr(ord(x)-32)
        else:
            s+=x
    return s


#lower()
def s_lower(st):
    s=""
    for x in st:
        if ord(x)>=65 and ord(x)<=90:
            s+=chr(ord(x)+32)
        else:
            s+=x
    return s       


#istitle()
def title_t(st):
    result = ""
    capitalize1 = True

    for char in st:
        if ord(char) >= 97 and ord(char) <= 122:
            if capitalize1:
                char = chr(ord(char) - 32)
                capitalize1 = False
        elif char in [" ", "-", "_"]:
            capitalize1 = True
        result += char

    return result

#capitalize()

def capitalize_s(st):
    s=""
    for x in range(len(st)):
        if x==0:
            if ord(st[0])<=122 and ord(st[0])>=97:
                s+=chr(ord(st[0])-32)
            else:
                s+=st[x]
        else:
            if st[x-1]==" ":
                if ord(st[x])<=122 and ord(st[x])>=97:
                    s+=chr(ord(st[x])-32)
                    continue
                else:
                    s+=st[x]
                    continue
            elif ord(st[x])>=65 and ord(st[x])<=90:
                s+=chr(ord(st[x])+32)
            else:
                s+=st[x]
    return 

#swapcase()

def swapcase_s(st):
    s1=""
    for y in st:
        if ord(y)>=65 and ord(y)<=90:
            s1+=chr(ord(y)+32)
        elif ord(y)>=97 and ord(y)<=122:
            s1+=chr(ord(y)-32)
        else:
            s1+=y
    return s1  



    