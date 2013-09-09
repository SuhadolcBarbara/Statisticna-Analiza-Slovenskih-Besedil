import os, sys
import re


os.chdir("C:\Users\Quill\Desktop\DIPLOMA\Wikipedija\Tabela\SkTabela\\") #pot do korpusa
list = file("1SkupnaTabela.txt", "rt")

tableOfLength = []
dicOfWords = dict([])
stBesed = 0

f = list.read()
list.close()
lines = f.split("\n")
lines = filter(None, lines)
for line in lines:
    seperatedLine = line.split("\t")
    leng = len(seperatedLine[0])
    if leng == 0:
        continue
    if leng > 22:
        print line
    stBesed = stBesed + 1
    if leng not in tableOfLength:
        tableOfLength.append(leng)
        dicOfWords[leng] = 1
    else:
        dicOfWords[leng] = dicOfWords[leng] + 1

text = file("DolzineBesed.txt", "wt")
for theWordLen in dicOfWords:
    theNum = dicOfWords[theWordLen]
    text.write("%i\t%i\n" %(theWordLen, theNum))

text.close()    
print stBesed