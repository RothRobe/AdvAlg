preis = [1, 5, 8, 9]


def greedy():
    preisprometer = []

    for i in range(4):
        preisprometer.append(preis[i] / i)

    print(preisprometer)


def Stangenzerlegung(n=len(preis)):
    if n == 0:
        return 0
    q = -1
    for i in range(n):
        q = max(q, preis[i] + Stangenzerlegung(n - (i + 1)))
    return q


# print(Stangenzerlegung())

def MemoStangenzerlegung(n=len(preis)):
    e = []
    e.append(0)
    for i in range(1, n):
        e.append(-1)
    return HauptStangenzerlegung(n, e)


def HauptStangenzerlegung(n, e):
    if n - 1 == -1:
        return 0
    if e[n - 1] > -1:
        return e[n - 1]
    q = -1
    for i in range(n):
        q = max(q, preis[i] + HauptStangenzerlegung(n - (i + 1), e))
        e[n - 1] = q
    return q


def BottomUpStangenzerlegung():
    e = []
    n = len(preis)

    for k in range(n):
        e.append(-1)

    for j in range(n):
        q = -1
        for i in range(j + 1):
            if (j - (i + 1)) < 0:
                q = max(q, preis[i] + 0)
            else:
                q = max(q, preis[i] + e[j - (i + 1)])
        e[j] = q
    return q


#print(BottomUpStangenzerlegung())


def ErweiterteBottomUpZerlegung():
    l = []
    e = []
    n = len(preis)

    for k in range(n):
        e.append(-1)
        l.append(-1)

    for j in range(n):
        q = -1
        for i in range(j + 1):
            e2 = 0 if j - (i + 1) < 0 else e[j - (i + 1)]
            if q < preis[i] + e2:
                q = preis[i] + e2
                l[j] = i+1
        e[j] = q

    while n > 0:
        print(l[n-1])
        n = n - l[n-1]



#def GibZerlegungAus():
#    ErweiterteBottomUpZerlegung(e, l, n)

ErweiterteBottomUpZerlegung()