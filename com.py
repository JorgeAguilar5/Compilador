# -*- enconding: utf-8 -*-
import os
from COM.c_lexer import Analizador_lexico
import ply_build.armar as construir


def menu():
    opcion = 0
    while (opcion != 8):
        os.system("cls")
        print ('''MENU COMPILADOR
         \t1: Programa Fuente
         \t2: Analizador Lexico
         \t3: Analizador Sintactico
         \t4: Convertir a Codigo Objeto (.O)
         \t5: Convertir a Codigo ASEMBLER (.S)
         \t6: Convertir a Codigo EXE    (.BIN)
         \t7: Ejecutar Programa
         \t8: Salir''')
        opcion =int(input("opcion: "))
        if opcion == 1:
            print ("Programa Fuente")
            fuente = input("fuente: ")
            os.system("notepad.exe" + fuente)
        elif opcion == 2:
            print ("Analizador Lexico")
            Analizador_lexico()
            os.system("pause")
        elif opcion == 3:
            print ("Analizador Sintactico")
            construir.Analizador_sintacito();
            os.system("pause")
        elif opcion == 4:
            print ("Convetit A Codigo Objeto")
            construir.OBJ()
        elif opcion == 5:
            print ("Convetit A Codigo Objeto")
            construir.ASEMBLER()
        elif opcion == 6:
            print ("Convetit A Codigo EXE")
            construir.EXE()
        elif opcion == 7:
            print ("Ejecutar programa")
            construir.RUN()
        elif opcion == 8:
            print ("gracias por usar este programa")
        else:
            print ("error")
    pass

if __name__ == '__main__':
    menu()
