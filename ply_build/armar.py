# -*- enconding: utf-8 -*-
import os


def Analizador_sintacito():
    a = input("direccion: ")
    if (os.path.exists(a)):
        os.system("g++ -Wall -c    " + a)
        if (os.path.exists("*.o")):
            os.system("del *.o")
    else:
        print ("Error en el nombre del archivo")


def OBJ():
    a = input("direccion: ")
    if (os.path.exists(a)):
        os.system("g++ -Wall -c " + a)
        os.system("pause")


def EXE():
    a = input("direccion: ")
    if (os.path.exists(a)):
        os.system("g++ -Wall -o " + "exe " + a)
        os.system("pause")
    

def RUN():
    os.system("exe.exe")

