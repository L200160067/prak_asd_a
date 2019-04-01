class MhsTIF():
    def __init__(self, nim):
        self.nim = nim

    def __str__(self):
        return str(self.nim)
    
c0 = MhsTIF(1000)
c1 = MhsTIF(1051)
c2 = MhsTIF(1002)
c3 = MhsTIF(1018)
c4 = MhsTIF(1004)
c5 = MhsTIF(1031)
c6 = MhsTIF(1013)
c7 = MhsTIF(1006)
c8 = MhsTIF(1024)
c9 = MhsTIF(1064)
c10 = MhsTIF(1039)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


#No.1
def bubbleSort():
    n = len(Daftar)
    for i in range (n-1):
        for j in range (n-i-1):
            if Daftar[j].nim > Daftar[j+1].nim:
                swap(Daftar,j,j+1)
    Daftar2 = [Daftar[0].nim, Daftar[1].nim, Daftar[2].nim, Daftar[3].nim, Daftar[4].nim, Daftar[5].nim, Daftar[6].nim, Daftar[7].nim, Daftar[8].nim, Daftar[9].nim, Daftar[10].nim]
    print (Daftar2)


#No.2
A = [1, 3, 5, 7, 9]
B = [2, 4, 6, 8, 10]
C = []

def gabung():
    C.extend(A)
    C.extend(B)
    n = len(C)
    for i in range (n-1):
        for j in range (n-i-1):
            if C[j] > C[j+1]:
                swap(C,j,j+1)
    print (C)
from time import time as detak
from random import shuffle as kocok

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort(L):
    n = len(L)
    for i in range (n-1):
        for j in range (n-i-1):
            if L[j] > L[j+1]:
                swap(L,j,j+1)
    return L

def selectionSort(L):
    n = len(L)
    for i in range(n-1):
        indexKecil = cariPosisiTerkecil(L, i, n)
        if indexKecil != i:
            swap(L, i, indexKecil)
    return L

def insertionSort(L):
    n = len(L)
    for i in range(1, n):
        nilai = L[i]
        pos = i
        while pos > 0 and nilai < L[pos -1]:
            L[pos] = L[pos-1]
            pos = pos - 1
        L[pos] = nilai
    return L
        
daftar = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print (bubbleSort(daftar))
print (selectionSort(daftar))
print (insertionSort(daftar))


k =  [[i] for i in range(1, 6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print("bubble: %g detik" %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print("selection: %g detik" %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print("insertion: %g detik" %(ak-aw));

L = [1000, 1051, 1002, 1018, 1004, 1031, 1013, 1006, 1024, 1064, 1039]

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort():
    n = len(L)
    for i in range (n-1):
        for j in range (n-i-1):
            if L[j] > L[j+1]:
                swap(L,j,j+1)

def selectionSort():
    n = len(L)
    for i in range(n-1):
        indexKecil = cariPosisiTerkecil(L, i, n)
        if indexKecil != i:
            swap(L, i, indexKecil)

def insertionSort():
    n = len(L)
    for i in range(1, n):
        nilai = L[i]
        pos = i
        while pos > 0 and nilai L[pos -1]:
            L[pos] = L[pos-1]
            pos = pos - 1
        L[pos] = nilai
