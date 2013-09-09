#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, codecs

os.chdir("C:\Users\Quill\Desktop\DIPLOMA")

tabela = codecs.open("JoinedCorpus.txt", "r", encoding="utf-8")
r = tabela.read()
tabela.close()
dicOf3Gram = dict([])
triGram = []

rd = r.split("\n")

for line in rd:
    wordNNum = line.split("\t")
    word = wordNNum[0]
    wordLeft = word
    while(len(wordLeft) > 2):
        gram = wordLeft[:3]
        if gram in triGram:
            dicOf3Gram[gram] = int(dicOf3Gram[gram]) + 1
        else:
            dicOf3Gram[gram] = 1
            triGram.append(gram)
        wordLeft = wordLeft[1:]

table = file("3-gram.txt", "wt")
n = 0
i = 0

print len(dicOf3Gram)
for gram in dicOf3Gram:
    i = i + 1
    #print i
    string = "%s\t%i\n" %(gram, dicOf3Gram[gram])
    table.write(string.encode("utf-8"))
   
table.close()