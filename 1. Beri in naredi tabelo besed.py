#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import re
import codecs

def addToCrrntDic(nameTable, theWord, theNum):
    string = "%s\t%i\n" %(theWord, theNum)
    nameTable.write(string.encode("utf-8"))

def getCrke():
    f = file("C:\Users\Quill\Desktop\DIPLOMA\AllowedCrkeUTF.txt", "rt") #pot do seznama dovoljenih crk - da se izognemo napak na straneh, kopiranju, trubar 
    a = f.read().decode("utf-8")
    f.close()
    return a

def createTabela(text):
    table = file("C:\Users\Quill\Desktop\DIPLOMA\Wikipedija\Tabela\\" + text, "wt") #pot do podtabele - tabele rezultatov korpusa
    return table
        
# izpise vse datoteke v mapi
listOfTexts = os.listdir("C:\Users\Quill\Desktop\DIPLOMA\Wikipedija") #pot do korpusa
os.chdir("C:\Users\Quill\Desktop\DIPLOMA\Wikipedija") #pot do korpusa

canCrke = getCrke()

for text in listOfTexts:
    nameTable = createTabela(text)
    if text[-4:] != ".txt":
        continue
    f = codecs.open(text, "r", encoding="utf-8")
    #f = file(text, "rt")
    print text
    
    tableOfWords = []
    dicOfWords = dict([])

    for line in f:
        line = line.lower()
        line = line.strip()
        line = line.replace(']', ' ')
        line = line.replace('[', ' ')

        line = re.sub('[., )(-_»«!?"12&|¸34§$@%#567890=+<>:;\']', ' ', line)      #ce so se kake nesr.ece, dodaj v to vrstico
        listOfWords = line.split(' ')
        listOfWords = filter(None, listOfWords) #vrze prazne ven

        for word in listOfWords:
            #word = word.decode("utf-8")
            zeeWord = []
            for crka in word:
                if crka == "Č":
                    crka = "č"
                elif crka == "Ž":
                    crka = "ž"
                elif crka == "Š":
                    crka = "š"
                elif crka == "Ć":
                    crka = "ć"
                elif crka =="Ź":
                    crka = "ź"
                if crka in canCrke:
                    zeeWord.append(crka)
                word = "".join(zeeWord)
            if word not in tableOfWords:
                tableOfWords.append(word)
                dicOfWords[word] = 1
            else:
                dicOfWords[word] = dicOfWords[word] + 1
                
    for theWord in dicOfWords:
        theNum = dicOfWords[theWord]
        addToCrrntDic(nameTable, theWord, theNum)
    nameTable.close()