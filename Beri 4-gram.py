#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, codecs

os.chdir("C:\Users\Quill\Desktop\DIPLOMA")

tabela = codecs.open("JoinedCorpus.txt", "r", encoding="utf-8")
r = tabela.read()
tabela.close()
dicOf4Gram = dict([])
theDict = dict([])

stiriGram = []
rd = r.split("\n")

for line in rd:
    wordNNum = line.split("\t")
    word = wordNNum[0]
    wordLeft = word
    
    while(len(wordLeft) > 3):
        gram = wordLeft[:4]
        if gram in stiriGram:
            dicOf4Gram[gram] = int(dicOf4Gram[gram]) + 1
        else:
            dicOf4Gram[gram] = 1
            stiriGram.append(gram)
        wordLeft = wordLeft[1:]

table = file("4-gram.txt", "wt")
n = 0
i = 0

print len(dicOf4Gram)
for gram in dicOf4Gram:
    i = i + 1
    string = "%s\t%i\n" %(gram, dicOf4Gram[gram])
    table.write(string.encode("utf-8"))

print "END"    
   
table.close()