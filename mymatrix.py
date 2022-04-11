"""
mymatrix.py - moja implementacja funkcji macierzowych
"""
def getMatEl(i,j):
    """
    pobiera element do wiersza i, kolumny j macierz i robi konwersje do float
    """
    x=input("Podaj el. {w}x{k}: ".format(w=i+1,k=j+1))
    while not x.isdigit():
        if len(x)>0:
            if x[0].isdigit() or x[0]=='-':
                break
        print('Błąd!\n')
        x=input("Podaj el. {w}x{k}: ".format(w=i+1,k=j+1))
    return float(x)

def mat():
    """
    macierz złożona za pomocą listy składanej, bez konwersji typu danych, wszystko jako string
    """
    col=input("Podaj ilość kolumn: ")
    while not col.isdigit() or int(col)<=0:
        print("Błąd!")
        col=input("Podaj ilość kolumn: ")
    row=input("Podaj ilość wierszy: ")
    while not row.isdigit() or int(row)<=0:
        print("Błąd!")
        row=input("Podaj ilość wierszy: ")
    return [[getMatEl(c,r) for r in range(int(col))] for c in range(int(row))]#wypełnia funkcja getMatEl wiersze macierzy

def showMacierz(m):
    """
    wyswietla podana macierz
    """
    if isinstance(m,list):
        for i in range(len(m)):
            for j in m[i]:
                print('\t',j,end='')
            print()
    else:
        print("Błąd!")

def sumMacierz(a,b,char):
    """
    liczy sume lub roznice podanych macierzy, trzeci argument '+'/'-' okresla dzialanie
    """
    if len(a)==len(b) and len(a[0])==len(b[0]):
        suma=[]
        for i in range(len(a)):
            row=[]
            for j in range(len(a[0])):
                if char=='+':
                    row.append(a[i][j]+b[i][j])
                elif char=='-':
                    row.append(a[i][j]-b[i][j])
            suma.append(row)
        showMacierz(suma)
    else:
        print('Błąd! Niepoprawne dane!')

def mnozMacierze(a,b):
    """
    mnozy macierze
    """
    if isinstance(a,list) and isinstance(b,list):
        print('A:\n')
        showMacierz(a)
        print('B:\n')
        showMacierz(b)
        if len(a[0])==len(b):
            m=[]
            for i in range(len(a)):
                row=[]
                sum=0
                for k in range(len(b[0])):
                    for j in range(len(b[0])):
                        sum+=a[i][j]*b[j][k]
                    row.append(sum)
                    sum=0
                m.append(row)
            print('A*B:\n')
            showMacierz(m)
        else:
            print('Błąd!\nNiezdefiniowano!\n')
    else:
        print('Błędne dane\n')

def skalarMat(a,b):
    """
    mnozy macierz przez liczbe
    """
    if isinstance(a,list):
        print('Macierz A:')
        showMacierz(a)
        print('A * ',b)
        showMacierz([[a[r][c]*b for c in range(len(a[0]))] for r in range(len(a))]) #r- wiersz, c-kolumna
    else:
        print(a*b)
        
def tMat(a):
    """
    Transpozycja macierzy
    """
    if isinstance(a,list):
        print('Macierz A:')
        showMacierz(a)
        print('Transponowane A:')
        showMacierz([[a[c][r] for c in range(len(a))] for r in range(len(a[0]))])
    else:
        print('Niezdefiniowano!')

if __name__=='__main__':
    sumMacierz(mat(),mat(),'+')
    sumMacierz(mat(),mat(),'-')
    mnozMacierze(mat(),mat())
    skalarMat(mat(),2)
    tMat(mat())
