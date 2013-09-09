#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os, re, codecs

os.chdir("C:\Users\Quill\Desktop\DIPLOMA\Castniki\Tabela\SkTabela") #pot do korpusa


tabelaCrk = []
allCrke = file("C:\Users\Quill\Desktop\DIPLOMA\AllowedCrkeUTFInterested.txt", "rt") #pot do allowedCrke
tabeCrk = allCrke.read().decode("utf-8")
allCrke.close()
for crka in tabeCrk:
    tabelaCrk.append(crka)

tabela = file("1SkupnaTabela.txt", "rt")
tabelaBesed = tabela.read().decode("utf-8")
tabela.close()


#polozaj = {'0':0, '1':0, '-1': 0, '-2':0}
polozaj = []
crke = dict()

for crka in tabelaCrk:
    #0 = 0; 1 = 1; 2 = -2; 3 = -1 
    crke[crka] = {}
    crke[crka][0] = 0
    crke[crka][1] = 0
    crke[crka][2] = 0
    crke[crka][3] = 0
lines = tabelaBesed.split("\n")
for line in lines:
    word = line.split("\t")[0]
    dolzinaBesede = len(word)
    #if(dolzinaBesede > 4):
    for crka in tabelaCrk:
        if crka in word:
            if dolzinaBesede > 1 and word[0] == crka:
                crke[crka][0] = int(crke[crka][0]) + 1
            if dolzinaBesede > 2 and word[1] == crka:
                crke[crka][1] = int(crke[crka][1]) + 1
            if dolzinaBesede > 3 and word[-2] == crka:
                crke[crka][2] = int(crke[crka][2]) + 1
            if dolzinaBesede > 1 and word[-1] == crka:
                crke[crka][3] = int(crke[crka][3]) + 1
                
    


#print crke

pisi = file("polozajCrk.txt", "wt")
string1 = "crka\t0\t1\t-2\t-1\n"
pisi.write(string1.encode("utf-8"))
for crka in crke:
    string2 = crka + "\t"
    pisi.write(string2.encode("utf-8"))
    for pol in crke[crka]:
        #pisi.write("\t " + str(pol) + " ")
        string3 = "%s\t" %(crke[crka][pol])
        pisi.write(string3.encode("utf-8"))
    string4 = "\n"
    pisi.write(string4.encode("utf-8"))
pisi.close()    