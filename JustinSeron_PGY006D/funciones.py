import numpy
import os
import msvcrt
from colorama import Style, Fore, Back
import random

#Arreglo
alumno = numpy.empty([10,8],object)

#Diseño
def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")
    

def printv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")
    

def printa(texto):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")
    

#Lista Notas
listaNotas = []
listaNotas.append("1.0")
listaNotas.append("1.5")
listaNotas.append("2.0")
listaNotas.append("2.5")
listaNotas.append("3.0")
listaNotas.append("3.5")
listaNotas.append("4.0")
listaNotas.append("4.5")
listaNotas.append("5.0")
listaNotas.append("5.5")
listaNotas.append("6.0")
listaNotas.append("6.5")
listaNotas.append("7.0")

#Limpiar Pantalla
def limpiarpantalla():
    printa("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system('cls')

#Validar Rut
def validarRut(rut):
    for i in range(10):
        if alumno[i,0]==rut:
            return i
    return -1

def registrar(rut,nCompleto,edad,genero,promedio,fecMatricula,nApoderado):
    if validarRut(rut)<0:
        if len(nCompleto) >= 2:
            if edad >= 4:
                for i in range(10):
                    if alumno[i,0]==None:
                        alumno[i,0]=rut
                        alumno[i,1]=nCompleto
                        alumno[i,2]=edad
                        alumno[i,3]=genero
                        alumno[i,4]=promedio
                        alumno[i,5]=fecMatricula
                        alumno[i,6]=nApoderado
                        break
            else:
                printr("La edad no puede ser menor a 4")
        else:
            printr("El nombre no puede tener menor de 2 carácteres")
    else:
        printr("RUT Repetido")

def buscarAlumno(rut):
    indice = validarRut(rut)
    if indice>= 0:
        print(f"""
        ALUMNO RUT      : {alumno[indice,0]}
        NOMBRE COMPLETO : {alumno[indice,1]}
        EDAD            : {alumno[indice,2]}
        GENERO          : {alumno[indice,3]}
        PROMEDIO FINAL  : {alumno[indice,4]}
        FECHA MATRICULA : {alumno[indice,5]}
        NOMBRE APODERADO: {alumno[indice,6]}""")
    else:
        printr("RUT no registrado")

#Certificados

#Anotaciones
listaAnotaciones = []
listaAnotaciones.append("Alumno muy responsable")
listaAnotaciones.append("Alumno irresponsable")
listaAnotaciones.append("Alumno demasiado revoltoso")
listaAnotaciones.append("Alumno limpia toda la sala por su cuenta")
listaAnotaciones.append("Alumno muy brillante")
listaAnotaciones.append("Sáquenme de su sala")
listaAnotaciones.append("Alumno rompe ventana con querer")
listaAnotaciones.append("Alumno le hace broma de mal gusto al profesor")
listaAnotaciones.append("Alumno copia durante la prueba N°3 de matemáticas")
listaAnotaciones.append("Alumno genera conflicto masivo entre sus compañeros")

def anotaciones(rut):
    indice = validarRut(rut)
    if indice >= 0:
        print(f"""
        {Fore.YELLOW}{Style.BRIGHT}CERTIFICADO ANOTACIONES{Fore.RESET}{Style.RESET_ALL}
        --------------------------
        RUT   : {alumno[indice,0]}
        NOMBRE: {alumno[indice,1]}
        --------------------------
        Anotación 1: {listaAnotaciones[random.randint(0,9)]}
        Anotación 2: {listaAnotaciones[random.randint(0,9)]}
        Anotación 3: {listaAnotaciones[random.randint(0,9)]}""")
    else:
        printr("RUT no registrado")

#Notas
def notas(rut):
    indice = validarRut(rut)
    if indice >= 0:
        print(f"""
        {Fore.YELLOW}{Style.BRIGHT}CERTIFICADO NOTAS{Fore.RESET}{Style.RESET_ALL}
        --------------------------
        RUT   : {alumno[indice,0]}
        NOMBRE: {alumno[indice,1]}
        --------------------------
        Nota Lenguaje   : {listaNotas[random.randint(0,12)]}
        Nota Matemáticas: {listaNotas[random.randint(0,12)]}
        Nota Inglés     : {listaNotas[random.randint(0,12)]}
        Nota Historia   : {listaNotas[random.randint(0,12)]}""")
    else:
        printr("RUT no registrado")

def regular(rut):
    indice = validarRut(rut)
    if indice >= 0:
        print(f"""
        {Fore.YELLOW}{Style.BRIGHT}CERTIFICADO ALUMNO REGULAR{Fore.RESET}{Style.RESET_ALL}
        ---------------------------
        El o la estudiante {Fore.GREEN}{alumno[indice,1]} RUT {alumno[indice,0]}{Fore.RESET} se encuentra efectivamente matriculado
        en la institución {Fore.YELLOW}{Style.BRIGHT}"San Charlis"{Fore.RESET}{Style.RESET_ALL}
        """)
    else:
        printr("RUT no registrado")


