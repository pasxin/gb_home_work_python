def neg_fibonachi (n):
    
    if n == -1:
        resultat = 1
        return resultat
    elif n == -2:
        resultat = -1
        return resultat
    else:
        resultat = neg_fibonachi (n+2) - neg_fibonachi (n+1)
        return resultat

def pos_fibonachi (n):
    if n == 0:
        resultat = 0
        return resultat
    elif n == 1:
        resultat = 1
        return resultat
    else:
        resultat = pos_fibonachi (n-1) + pos_fibonachi (n-2)
        return resultat



list = []
for i in range (-10,11):
    if i < 0:
        list.append (neg_fibonachi(i))
    else:
        list.append(pos_fibonachi(i))
print (list)