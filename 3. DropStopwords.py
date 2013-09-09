#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os, re, codecs

def saveNewDic(dicRead):
    endFile = file("Tabela\SkTabela\NoStopwords.txt", "wt") #ciljna pot
    for key in dicRead:
        string = "%s\t%i\n" %(key, dicRead[key])
        endFile.write(string)
    endFile.close()

def saveSW(dicRead):
    endFile = file("Tabela\SkTabela\SW.txt", "wt") #ciljna pot
    for key in dicRead:
        string = "%s\t%i\n" %(key, dicRead[key])
        endFile.write(string)
    endFile.close()    

def readTabela():
    f = file("Tabela\SkTabela\\1SkupnaTabela.txt", "rt")
    read = f.read()
    f.close()
    lines = read.split("\n")
    lines = filter(None, lines)
    for line in lines:
        line = line.split("\t")
        word = line[0]
        theNum = int(line[1])
        dicRead[word] = theNum
    return dicRead

def readStopWords ():
    stopwords = file("C:\Users\Quill\Desktop\DIPLOMA\STOPWORDS.txt", "rt")
    readSW = stopwords.read()
    stopwords.close()
    word = readSW.split("\n")
    return word


os.chdir("C:\Users\Quill\Desktop\DIPLOMA\Castniki\\") #pot do korpusa
dicRead = dict([])
dicRead = readTabela()
stopwords = readStopWords()
dicWrite = dict([])
dicSW = dict([])
sW = 0

for word in dicRead:
    isIN = 0
    for SW in stopwords:
        if word == SW:
            dicSW[word] = dicRead[word]
            sW = sW + int(dicRead[word])
            isIN = 1
    if isIN == 0:
        dicWrite[word] = dicRead[word]

saveNewDic(dicWrite)
saveSW(dicSW)
print sW
        
    