import funciones as fu
from colorama import Fore, Style

while True:
    fu.limpiarpantalla()
    print("""
    1) Registrar Alumno
    2) Buscar Alumno
    3) Certificados
    0) Salir""")
    opcion = int(input("Seleccione: "))

    if opcion == 0:
        fu.printv("Adiós...")
        break
    elif opcion == 1:
        fu.printa("REGISTRAR ALUMNO")
        rut = int(input("Digite RUT del alumno: "))
        nom = input("Ingrese nombre completo del alumno: ").capitalize()
        edad = int(input("Digite edad del alumno: "))
        genero = input("Señale si el alumno es 'Masculino' o 'Femenino': ").capitalize()
        nota = float(input("Promedio FINAL del alumno: "))
        fecha = input(f"Señale la fecha de matricula con {Fore.GREEN}{Style.BRIGHT}'dd/mm/yyyy'{Fore.RESET}{Style.RESET_ALL}: ")
        nApod = input("Nombre y Apellido del apoderado: ").capitalize()
        fu.registrar(rut,nom,edad,genero,nota,fecha,nApod)
    elif opcion == 2:
        fu.printa("BUSCAR ALUMNO")
        rut = int(input("RUT del alumno a buscar: "))
        fu.buscarAlumno(rut)
    elif opcion == 3:
        fu.printa("CERTIFICADOS")
        print("""
        1) Anotaciones
        2) Notas
        3) Alumno Regular""")
        opcion = int(input("Seleccione: "))
        if opcion == 1:
            rut = int(input("RUT del alumno a buscar: "))
            fu.anotaciones(rut)
        elif opcion == 2:
            rut = int(input("RUT del alumno a buscar: "))
            fu.notas(rut)
        elif opcion == 3:
            rut = int(input("RUT del alumno: "))
            fu.regular(rut)
        else:
            fu.printr("Opción no válida")
    else:
        fu.printr("Opción no válida")

