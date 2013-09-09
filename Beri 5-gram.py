#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, codecs

os.chdir("C:\Users\Quill\Desktop\DIPLOMA")

tabela = codecs.open("JoinedCorpus.txt", "r", encoding="utf-8")
r = tabela.read()
tabela.close()
dicOf5Gram = dict([])
petGram = []

rd = r.split("\n")

for line in rd:
    wordNNum = line.split("\t")
    word = wordNNum[0]
    wordLeft = word
    while(len(wordLeft) > 4):
        gram = wordLeft[:5]
        if gram in petGram:
            dicOf5Gram[gram] = int(dicOf5Gram[gram]) + 1
        else:
            dicOf5Gram[gram] = 1
            petGram.append(gram)
        wordLeft = wordLeft[1:]

table = file("5-gram.txt", "wt")
n = 0
i = 0

print len(dicOf5Gram)
for gram in dicOf5Gram:
    i = i + 1
    string = "%s\t%i\n" %(gram, dicOf5Gram[gram])
    table.write(string.encode("utf-8"))

print "END"   
table.close()