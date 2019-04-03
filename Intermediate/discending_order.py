
def Descending_Order(num):
    #Bust a move right here
    result=sorted(str(num),reverse=True)
    joined=''.join(result)
    return int(joined)

# Descending_Order(20887491383)
def is_triangle(a, b, c):
    if a!=0 and b!=0 and c!=0:
        return True
    else:
        return False
