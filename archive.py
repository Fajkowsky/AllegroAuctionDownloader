# -*- coding: utf8 -*-
import urllib, os

def saveCode():
    print '''
    ======================================================
    Wprowadz numer aukcji która ma zostać pobrana.
    '''
    number = raw_input("    Numer: ")
    
    try:
        number = int(number)
    except:
        print("    Wpisana wartość nie jest liczbą!")
    connectToServer(number)
    raw_input("    Nacisnij [enter] aby powrócić do menu.")

def connectToServer(number):
    fileHandle = None
    try:
        fileHandle = urllib.urlopen('http://allegro.pl/show_item.php?item=' + str(number))
    except:
        print("    Brak internetu lub błąd numeru aukcji.")
    downloadCode(fileHandle)
    
def downloadCode(fileHandle):
    fileName, code = "", ""
    titleAppear = False
    firstField, secondField = False, False
    
    for lines in fileHandle.readlines():
        if (not titleAppear and "<title>" in lines):
            fileName = lines[8:(lines.index(" - "))]
            titleAppear = True
        
        if(not firstField and "<fieldset id=" in lines):
            firstField = True
            print(lines)
        elif(not secondField and "</fieldset>" in lines and firstField):
            secondField = True
            print(lines)
        if(firstField and not secondField):
            code += lines

    saveFile(fileName, code)
    
def saveFile(fileName, code):
    try:
        text_file = open(fileName + ".html" , "w")
    except:
        print("    Nie można utworzyć pliku!")
    try:
        text_file.write(code)
        print("    Zapisano!")
    except:
        print("    Nie można zapisać pliku!")
    text_file.close()    
    
def getList():
    archieveList = []
    filesList = os.listdir(os.curdir)
    for item in filesList:
        if item.endswith(".html"):
            archieveList.append(item)
    print '''
    ======================================================
    Lista archiwalnych aukcji:
    '''
    for item in archieveList:
        print("    " + item)    
    raw_input("    Nacisnij [enter].")