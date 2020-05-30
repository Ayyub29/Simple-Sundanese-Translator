import nltk
import os
import re
import util
import sys

#Database = txt
#Database = Array of Kata2 dalam Database

def databaseMaker(Database):
    Database_split = Database.split("=")
    count = 0
    Database = Database_split
    for i in Database_split:
        Database[count] = i.strip()
        count += 1
    return Database

def kataIndexFinder(Kata, Database):
    count = 0
    for words in Database:
        if (str(words) == str(Kata)):
            return count
        else:
            if (count < len(Database)):
                count += 1
            else:
                count = -1
                return count

def terjemahkan(Kata,Database):
    itr = kataIndexFinder(Kata,Database)
    return Database[itr+1]

def cariDiDatabase(Kata, Database):
    Ada = False
    for words in Database:
        if (str(words) == str(Kata)):
            Ada = True
    return Ada

def cekPolaKalimat(Kata,Database):
    Ada = False
    for words in Database:
        if (searchWithKMP(words,Kata)):
            Ada = True
    return Ada

def cekKataValid(Kata):
    Ada = False
    if (Kata[len(Kata)-1] == " "):
        Ada = True
    return Ada

def searchWithKMP(Pattern, File):
    #Instansiasi Variabel
    PatternLength = len(Pattern) 
    FileLength = len(File)
    cntPattern = 0
    cntFile = 0
    Ada = False

    Prefix = [0]*PatternLength

    borderFunction(Pattern, Prefix)
    while ( cntFile < FileLength ):
        if (Pattern[cntPattern] == File[cntFile] ):
            cntFile += 1
            cntPattern += 1
        if ( cntPattern == PatternLength ):
            Ada = True
            cntPattern = Prefix[cntPattern-1]
        elif cntFile < FileLength and Pattern[cntPattern] != File[cntFile]: 
            if cntPattern != 0: 
                cntPattern = Prefix[cntPattern-1] 
            else: 
                cntFile += 1
    return Ada


def borderFunction(Pattern, Prefix):
    # Fungsi yang mengembalikan nilai border Function dari suatu Pattern
    # Masukan : String Pattern
    # Keluaran : List of Integer yang berisi 
    PatternLength = len(Pattern) 
    cntPrefix = 0
    Prefix[0]
    cntSuffix = 1
    while ( cntSuffix < PatternLength):
        if (Pattern[cntSuffix] == Pattern[cntPrefix]):
            cntPrefix +=1
            Prefix[cntSuffix] = cntPrefix
            cntSuffix += 1
        else:
            Prefix[cntSuffix] = 0
            cntSuffix += 1


def terjemahkanKalimat(Kalimat,Database):
    #Instansiasi Variabel
    KalimatLength = len(Kalimat) 
    cntKalimat = 0
    kataCurr = ""
    kalimatHasilTerjemah = ""
    Ada = False
    while (cntKalimat < KalimatLength ):
        kataCurr += Kalimat[cntKalimat]
        if ((cekKataValid(kataCurr)) or (cntKalimat == (KalimatLength -1))):
            Ada = cariDiDatabase(kataCurr.strip(),Database)
            if (Ada):
                tempKalimatHasil = kalimatHasilTerjemah 
                kalimatHasilTerjemah += terjemahkan(kataCurr.strip(),Database).strip() + " "
                kataCurr = ""
            else:
                Ada = cekPolaKalimat(kataCurr,Database)
                if (cntKalimat == (KalimatLength -1)):
                    kalimatHasilTerjemah += kataCurr.strip()
                    kataCurr = ""
                else:
                    if (Ada):
                        temp = kataCurr.strip().split(" ")
                        for katakata in temp:
                            if (cariDiDatabase(katakata,Database)):
                                kalimatHasilTerjemah += terjemahkan(katakata,Database).strip() + " "
                            else:
                                kalimatHasilTerjemah += katakata.strip() + " "
                        kataCurr = ""
        cntKalimat += 1
    return kalimatHasilTerjemah

namaKamus = "indonesia.txt"

pathKamus = '../kamus/' #Untuk Ubuntu
pathKamus2 = '..\\kamus\\' #Untuk Windows

try:
    pathKamus += namaKamus
    txtFile = open(pathKamus) #Untuk Ubuntu
except:
    pathKamus2 += namaKamus
    txtFile = open(pathKamus2) #Untuk Windows
txt = txtFile.read().replace("\n", " = ")


kalimat = ""
for j in range(len(sys.argv)):
    if (j == (len(sys.argv) - 1)):
        kalimat += sys.argv[j]
    else:
        if (j > 0):
            kalimat += sys.argv[j]
            kalimat += " "
            
Bacod = databaseMaker(txt)
inter = terjemahkanKalimat(kalimat,Bacod)

print(inter)