#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, codecs

os.chdir("C:\Users\Quill\Desktop\DIPLOMA\Wikipedija\Tabela\SkTabela\\") #pot do korpusa

tabela = codecs.open("1SkupnaTabela.txt", "r", encoding="utf-8")
print type(tabela)
r = tabela.read()
tabela.close()
dicOf2Gram = dict([])
dvaGram = []

rd = r.split("\n")

for line in rd:
    wordNNum = line.split("\t")
    word = wordNNum[0]
    wordLeft = word
    while(len(wordLeft) > 1):
        gram = wordLeft[:2]
        if gram in dvaGram:
            dicOf2Gram[gram] = int(dicOf2Gram[gram]) + 1
        else:
            dicOf2Gram[gram] = 1
            dvaGram.append(gram)
        wordLeft = wordLeft[1:]

table = file("2-gram.txt", "wt")
print type(table)
n = 0
i = 0

print len(dicOf2Gram)
for gram in dicOf2Gram:
    i = i + 1
    string = "%s\t%i\n" %(gram, dicOf2Gram[gram])
    table.write(string.encode('utf-8'))
table.close()