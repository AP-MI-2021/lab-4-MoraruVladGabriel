def citirelista():
    list = []
    givenString = input("Dati elemtele listei, separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        list.append(int(x))
    return list


def nr_neg(lista):
    '''
    Creaza o noua lista cu toate numerele negative din lista data.
    :param lista: lista data
    :return: o noua lista cu toate numerele negative din lista data
    '''
    list = []
    for x in lista:
        if x < 0:
            list.append(x)
    return list


def cel_mai_mic_nr_cu_ultima_cifra_data(lista, cifra):
    '''
    Determina cel mai mic numar din lista care are ultima cifra egala cu o cifra data.
    :param lista: lista data
    :param cifra: cifra data.
    :return: numarul cerut.
    '''

    list = []

    for x in lista:
        if x % 10 == cifra:
            list.append(x)
    if len(list) == 0:
        return -1
    else:
        mini = list[0]
        for x in list:
            if x < mini:
                mini = x
        return mini


def isPrime(x):
    '''
    Veridica daca un numar este prim
    :param x: numarul dat, int
    :return: True, daca numarul este prim, False, daca numarul nu este prim.
    '''
    if x<2:
        return False
    if x==2:
        return True
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    return True


def isSuperprim(x):
    '''
    Verifica daca un numar este superprim.
    :param x: numarul dat.
    :return: True, daca numarul este superprim, False, daca numarul nu este superprim.
    '''
    nrcifre = 1
    copyx = x
    while copyx != 0:
        nrcifre = nrcifre * 10
        copyx = copyx // 10
    nrcifre = nrcifre // 10
    while nrcifre != 0:
        if isPrime(x % nrcifre) == False:
            return False
        nrcifre = nrcifre // 10
    return True


def cmmdc(x, y):
    '''
    Determina cmmdc ul a doua numere.
    :param x: primul numar
    :param y: al doilea numar.
    :return: cmmdc ul
    '''
    if x * y == 0:
        return x + y
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y -x
    return x


def cmmdc_lista(lista):
    '''
    determina cmmdc ul elemtelor unei liste
    :param lista: lista data
    :return: cmmdc ul
    '''
    if len(lista) < 2:
        return -1
    rez = cmmdc(lista[0], lista[1])
    for i in range(2,len(lista)):
        rez = cmmdc(rez, lista[i])
    return rez


def test_cmmdc_lista():
    assert cmmdc_lista([1]) == -1
    assert cmmdc_lista([2, 4, 6]) == 2
    assert cmmdc_lista([12, 24, 144]) == 12


def creare_lista_pozitiva(lista):
    '''
    Creaza o lista cu elemente pozitive.
    :param lista: lista data
    :return: lista cu elemente pozitive
    '''
    lstpoz = []
    for x in lista:
        if x > 0:
            lstpoz.append(x)
    return lstpoz


def og(x):
    '''
    oglindeste un nr
    :param x: numarul dat
    :return: oglinditul
    '''
    if x > -10 and x < 10:
        return x
    og = 0
    while x != 0:
        og = og * 10 + x % 10
        x = x // 10
    return og


def test_og():
    assert og(12) == 21
    assert og(2) == 2
    assert og(23) == 32


def inversare_nr_neg(x):
    '''
    inverseaza un numar.
    :param x: numarul dat.
    :return: inversul lui.
    '''
    nrpoz = -1 * x
    return -1*og(nrpoz)


def inlocuire_elemte(lista):
    '''
    numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    :param lista:lista data
    :return:noua lista
    '''

    lstpoz = creare_lista_pozitiva(lista)
    cmmdcpoz = cmmdc_lista(lstpoz)
    lstnou = []
    for x in lista:
        if x < 0:
            lstnou.append(inversare_nr_neg(x))
        else:
            lstnou.append(cmmdcpoz)
    return lstnou


def test_inlocuire_elemente():
    assert inlocuire_elemte([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]


def test_inversare_nr_neg():
    assert inversare_nr_neg(-12) == -21
    assert inversare_nr_neg(-13) == -31
    assert inversare_nr_neg(-24) == -42


def test_creare_lista_pozitiva():
    assert creare_lista_pozitiva([1,2,3]) == [1,2,3]
    assert creare_lista_pozitiva([1,2,-1]) == [1,2]
    assert creare_lista_pozitiva([-1,-2]) == []


def test_cmmdc():
    assert cmmdc(2, 4) == 2
    assert cmmdc(1, 5) == 1
    assert cmmdc(5, 25) == 5


def test_isSuperprim():
    assert isSuperprim(239) is True

def test_cel_mai_mic_nr_cu_ultima_cifra_data():
    assert cel_mai_mic_nr_cu_ultima_cifra_data([12, 13, 14, 15], 4) == 14
    assert cel_mai_mic_nr_cu_ultima_cifra_data([12, 12, 22, 14], 2) == 12
    assert cel_mai_mic_nr_cu_ultima_cifra_data([1, 9, 19, 20, 10, 50], 0) == 10
    assert cel_mai_mic_nr_cu_ultima_cifra_data([1, 2, 3],0) == -1


def test_nr_neg():
    assert nr_neg([-1, 2, -3]) == [-1, -3]
    assert nr_neg([1, 2]) == []
    assert nr_neg([-1, -6, -9]) == [-1, -6, -9]


def all_tests():
    test_nr_neg()
    test_cel_mai_mic_nr_cu_ultima_cifra_data()
   # test_isSuperprim()
    test_cmmdc()
    test_cmmdc_lista()
    test_creare_lista_pozitiva()
    test_og()
    test_inversare_nr_neg()
    test_inlocuire_elemente()


def printMenu():
    print("1.Citire lista(Dati elementele separate prin virgula): ")
    print("2.Afișarea tuturor numerelor negative nenule din listă:")
    print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură: ")
    print("4.Afișarea tuturor numerelor din listă care sunt superprime: ")
    print("5.Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu"
            "CMMDC-ul lor și numerele negative au cifrele în ordine inversă: ")
    print("x.Iesire.")


if __name__ == "__main__":
    all_tests()
    printMenu()
    lista = []
    while True:
        opt = input("Dati optiunea: ")
        if opt == '1':
            lista = citirelista()
        elif opt == '2':
            neglist = nr_neg(lista)
            print(f'toate numerele negative din lista sunt: {neglist}')
        elif opt == '3':
            cifra = int(input("Dati o cifra: "))
            mini = cel_mai_mic_nr_cu_ultima_cifra_data(lista, cifra)
            if mini == -1:
                print(f'nu exista cel mai mic element cu ultima cifra {cifra}')
            else:
                print(mini)
        elif opt == '4':
                pass
        elif opt == '5':
            inlocuire_elemte(lista)
        elif opt == 'x':
            break
        else:
            print("Optiune gresita!Reincercati.")
