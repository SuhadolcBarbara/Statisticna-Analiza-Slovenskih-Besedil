import os, sys

#poti do korpusov
tabelaNaslovov = ["C:\Users\Quill\Desktop\DIPLOMA\Proza\Tabela\SkTabela\\1SkupnaTabela.txt",
                  "C:\Users\Quill\Desktop\DIPLOMA\Poezija\Tabela\SkTabela\\1SkupnaTabela.txt",
                  "C:\Users\Quill\Desktop\DIPLOMA\Castniki\Tabela\SkTabela\\1SkupnaTabela.txt",
                  "C:\Users\Quill\Desktop\DIPLOMA\Blogi\Tabela\SkTabela\\1SkupnaTabela.txt",
                  "C:\Users\Quill\Desktop\DIPLOMA\Wikipedija\Tabela\SkTabela\\1SkupnaTabela.txt"]

dicOfWords = dict([])
tableOfWords = []
stBesed = 0
print "working"

for text in tabelaNaslovov:
    print text
    odpri = file(text, "rt")
    beri = odpri.read()
    odpri.close()
    lines = beri.split("\n")
    for line in lines:
        loci = line.split("\t")
        if len(loci) < 2:
            continue
        theNum = int(loci[1])
        word = loci[0]
        if word in tableOfWords:
            dicOfWords[word] = dicOfWords[word] + theNum
        else:
            dicOfWords[word] = theNum
            tableOfWords.append(word)
            stBesed = stBesed + 1

newFile = file("C:\Users\Quill\Desktop\DIPLOMA\JoinedCORPUS.txt", "wt")
for word in dicOfWords:
    newFile.write("%s\t%i\n" %(word, dicOfWords[word]))
newFile.close()
            