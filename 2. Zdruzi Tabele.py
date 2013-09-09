#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import re
import codecs
#import unicodedata

def saveNewDic(dicRead):
    endFile = file("SkTabela\\1SkupnaTabela.txt", "wt")
    for key in dicRead:
        string = "%s\t%i\n" %(key, dicRead[key])
        endFile.write(string.encode("utf-8"))
    endFile.close()

def readOsnovna():
    endFile = codecs.open("SkTabela\\1SkupnaTabela.txt", "r", encoding="utf-8")
    endRead = endFile.read()
    lines = endRead.split("\n")
    lines = filter(None, lines)

    for line in lines:
        line = line.split("\t")
        word = line[0]
        #word = word.decode("utf-8")
        if len(line) > 1:
            theNum = int(line[1])
            dicRead[word] = theNum
    endFile.close()
    return dicRead
        
# izpise vse datoteke v mapi
listOfTexts = os.listdir("C:\Users\Quill\Desktop\DIPLOMA\Wikipedija\Tabela") #pot do posameznih tabel korpusa
os.chdir("C:\Users\Quill\Desktop\DIPLOMA\Wikipedija\Tabela") #pot do posameznih tabel korpusa

zacni = file("SkTabela\\1SkupnaTabela.txt", "wt")
zacni.close()

for text in listOfTexts:
    if text[0] == "1":
        continue
    if text[-4:] != ".txt":
        continue
    print text
    dicUnread = dict([])
    dicRead = dict([])          #vsakic posebej sprazne, da se stvari ne prepisujejo

    dicRead = readOsnovna()     #preberi ze koncen file
    #openedFile = file(text, "rt")
    readingUnread = codecs.open(text, "r", encoding="utf-8")
    read = readingUnread.read()

    lines = read.split("\n")
    lines = filter(None, lines)
    for line in lines: #za dicUnread
        line = line.split("\t")
        word = line[0]
        word = word.replace(" ", "") #za slučajne zmote along the way
        theNum = int(line[1])
        dicUnread[word] = theNum
        
    for word in dicUnread:
        if word in dicRead:
            dicRead[word] = dicRead[word] + dicUnread[word]
        else:
            dicRead[word] = dicUnread[word]
    saveNewDic(dicRead)