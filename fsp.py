import copy
from itertools import permutations
import math
import timeit


def loadData(path):
    plik = open(path, "r")
    linie = plik.readlines()
    n = int(linie[0].split()[0])
    m = int(linie[0].split()[1])

    zadania = []
    for i in range(1, n+1):
        linia = linie[i].split()
        maszyny = []
        for j in range(1, 2*m, 2):
            maszyny.append(int(linia[j]))
        maszyny.append(i)
        zadania.append(maszyny)
    plik.close()

    return zadania

def getOrder(zad):
    kolejnosc = []
    for i in range(0, len(zad)):
        kolejnosc.append(zad[i][-1])
    return kolejnosc

def calculate_Cmax(zad):
    S = []
    C = []
    Szad = []
    Czad = []

    Szad.append(0)
    Czad.append(zad[0][0])

    for i in range(0, len(zad)):
        for j in range(0, len(zad[i])-1):
            if i == 0 and j != 0:
                Szad.append(Czad[j-1])
                Czad.append(Szad[j] + zad[i][j])
            elif i != 0:
                if j == 0:
                    Szad.append(C[i-1][0])
                    Czad.append(Szad[0] + zad[i][0])
                else:
                    Szad.append(max(Czad[j-1], C[i-1][j]))
                    Czad.append(Szad[j] + zad[i][j])

        S.append(Szad.copy())
        C.append(Czad.copy())
        Szad.clear()
        Czad.clear()

    return C[-1][-1]

def bruteForce(zad):
    perms = list(permutations(zad,r=len(zad)))
    Cmin = math.inf
    for perm in perms:
        C = calculate_Cmax(perm)
        if C < Cmin:
            Cmin = C
    return Cmin

zadania = loadData("data/data004.txt")

print(bruteForce(copy.deepcopy(zadania)))
