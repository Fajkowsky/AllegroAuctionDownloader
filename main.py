# -*- coding: utf8 -*-
import sys, archive, os

def cls():
    os.system("clear")
    
def menu():
    cls()
    print '''
    ==================ARCHIWIZER ALLEGRO==================
    Proszę wybrać odpowiednią liczbe:
    
    1 Archiwizuj wybraną aukcję.
    2 Lista archiwalnych aukcji.
    3 Coś innego
    
    0 Wyjście z programu.
    '''
    choice = raw_input("    Wybór: ")
    return choice 
    

def main():
    choice = ""
    while(choice <> "0"):
        choice = menu()
        if choice == "1":
            cls()
            archive.saveCode()
        elif choice == "2":
            cls()
            archive.getList()
        elif choice == "3":
            cls()
            print("Wybrałeś trojke.")
            raw_input("Nacisnij [enter].")
        elif choice != "0":
            cls()
            print("Wybrałeś nieprawidłow.")
            
    
if __name__ == '__main__':
    main()


