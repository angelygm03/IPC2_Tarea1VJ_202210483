from usuario import Usuario
from profesor import Profesor
from estudiante import Estudiante
import sys


profesores = []
estudiantes = []

def main():
    while True:

        print("----------------- Menú Principal -----------------")
        print("1. CRUD de Profesores")
        print("2. CRUD de Estudiantes")
        print("3. Salir")
        print("--------------------------------------------------")
        respuesta = input("Ingresa la acción que quieras realizar: ")
        print()

        if respuesta =="1":
            menu_crud_profesores()
        elif respuesta == "2":
            menu_crud_estudiantes()
        elif respuesta == "3":
            print("¡Hasta luego!")
            print()
            break
        else:
            print("Opción inválida. Inténtalo de nuevo")
            print()
    sys.exit()

#Menú profesores            
def menu_crud_profesores():
    print("----------------- Menú Profesores ----------------")
    print("1. Crear Profesor")
    print("2. Leer Profesores")
    print("3. Actualizar Profesor")
    print("4. Eliminar Profesor")
    print("5. Regresar al menú principal")
    print("--------------------------------------------------")
    respuestaProf = input("Ingresa la acción que quieras realizar: ")

    if respuestaProf =="1":
        crear_profesor()
    elif respuestaProf == "2":
        leer_profesores()
    elif respuestaProf == "3":
        actualizar_profesor()
    elif respuestaProf == "4":
        eliminar_profesor()
    elif respuestaProf == "5":
        print()
        main()
    else:
        print("Opción inválida. Inténtalo de nuevo")
        print()
        menu_crud_profesores()

def crear_profesor():
    print()
    print("----------------- Nuevo Profesor -----------------")
    nombre = input("Ingresa el nombre del profesor: ")
    curso = input("Ingresa el curso que imparte el profesor: ")

    while True:
        try:
            codigo = int(input("Ingresa el código del profesor: "))
            break
        except ValueError:
            print("Error: El código debe ser un número entero.")

    profesion = input("Ingresa la profesión del profesor: ")

    nuevo_profesor = Profesor(nombre, curso, codigo, profesion)
    profesores.append(nuevo_profesor)
    print("¡Profesor creado exitosamente!")
    print()
    menu_crud_profesores()

def leer_profesores():
    print()
    print('------------------- PROFESORES -------------------')
    if len(profesores) == 0:
        print('No hay profesores registrados en el programa')
        print()
        menu_crud_profesores()

    json_list = []
    for profesor in profesores:
        json_string = '''
{
    "nombre": "''' + profesor.nombre + '''",
    "curso": "''' + profesor.curso + '''",
    "codigo": "''' + str(profesor.codigo) + '''",
    "profesion": "''' + profesor.profesion + '''"
}'''
        json_list.append(json_string)
    
    json_output = '[\n' + ',\n'.join(json_list) + '\n]'
    print(json_output)
    menu_crud_profesores()
    print()

def actualizar_profesor():
    print()
    print("--------------- Actualizar Profesor ---------------")
    while True:
        try:
            codigo = int(input("Ingresa el código del profesor a actualizar: "))
            break
        except ValueError:
            print("Error: El código debe ser un número entero.")

    profesor_encontrado = None

    for profesor in profesores:
        if profesor.codigo == codigo:
            profesor_encontrado = profesor
            break

    if profesor_encontrado is None:
        print("Error: No se encontró un profesor con el código ingresado.")
        print()
        menu_crud_profesores()

    nombre = input("Ingresa el nuevo nombre del profesor: ")
    curso = input("Ingresa el nuevo curso que imparte el profesor: ")
    profesion = input("Ingresa la nueva profesión del profesor: ")

    profesor_encontrado.nombre = nombre
    profesor_encontrado.curso = curso
    profesor_encontrado.profesion = profesion

    
    print("¡Profesor actualizado exitosamente!")
    print()
    menu_crud_profesores()

def eliminar_profesor():
    print()
    print("---------------- Eliminar Profesor ----------------")
    while True:
        try:
            codigo = int(input("Ingresa el código del profesor que deseas eliminar: "))
            break
        except ValueError:
            print("Error: El código debe ser un número entero.")

    profesor_encontrado = None

    for profesor in profesores:
        if profesor.codigo == codigo:
            profesor_encontrado = profesor
            break

    if profesor_encontrado is None:
        print("Error: No se encontró un profesor con el código ingresado.")
        print()
        menu_crud_profesores()

    profesores.remove(profesor_encontrado)
    print("¡Profesor eliminado exitosamente!")
    print()
    menu_crud_profesores()

#Menú Estudiantes
def menu_crud_estudiantes():
    print("---------------- Menú Estudiantes ----------------")
    print("1. Crear Estudiante")
    print("2. Leer Estudiantes")
    print("3. Actualizar Estudiante")
    print("4. Eliminar Estudiante")
    print("5. Regresar al menú principal")
    print("--------------------------------------------------")
    respuestaEst = input("Ingresa la acción que quieras realizar: ")

    if respuestaEst =="1":
        crear_estudiante()
    elif respuestaEst == "2":
        leer_estudiantes()
    elif respuestaEst == "3":
        actualizar_estudiante()
    elif respuestaEst == "4":
        eliminar_estudiante()
    elif respuestaEst == "5":
        print()
        main()
    else:
        print("Opción inválida. Inténtalo de nuevo")
        print()
        menu_crud_estudiantes()

def crear_estudiante():
    print()
    print("---------------- Crear Estudiante ----------------")
    nombre = input("Ingresa el nombre del estudiante: ")
    curso = input("Ingresa el curso que cursa el estudiante: ")
    while True:
        try:
            carnet = int(input("Ingresa el carnet del estudiante: "))
            break
        except ValueError:
            print("Error: El carnet debe ser un número entero.")

    carrera = input("Ingresa la carrera del estudiante: ")

    nuevo_estudiante = Estudiante(nombre, curso, carnet, carrera)
    estudiantes.append(nuevo_estudiante)
    print("¡Estudiante creado exitosamente!")
    print()
    menu_crud_estudiantes()

def leer_estudiantes():
    print()
    print('------------------ ESTUDIANTES -------------------')
    if len(estudiantes) == 0:
        print('No hay estudiantes registrados en el programa')
        print()
        menu_crud_estudiantes()

    json_list = []
    for estudiante in estudiantes:
        json_string = '''
{
    "nombre": "''' + estudiante.nombre + '''",
    "curso": "''' + estudiante.curso + '''",
    "carnet": "''' + str(estudiante.carnet) + '''",
    "carrera": "''' + estudiante.carrera + '''"
}'''
        json_list.append(json_string)
    
    json_output = '[\n' + ',\n'.join(json_list) + '\n]'
    print(json_output)
    print()
    menu_crud_estudiantes()

def actualizar_estudiante():
    print()
    print('------------- Actualizar Estudiante --------------')
    try:
        carnet = int(input("Ingresa el carnet del estudiante que deseas actualizar: "))
    except ValueError:
        print("Error: El carnet debe ser un número entero.")
        print()
        menu_crud_estudiantes()

    estudiante_encontrado = None
    
    for estudiante in estudiantes:
        if estudiante.carnet == carnet:
            estudiante_encontrado = estudiante
            break
    
    if estudiante_encontrado is None:
        print("Error: No se encontró un estudiante con el carnet ingresado.")
        print()
        menu_crud_estudiantes()
    
    nombre = input("Ingresa el nuevo nombre del estudiante: ")
    curso = input("Ingresa el nuevo curso que toma el estudiante: ")
    carrera = input("Ingresa la nueva carrera del estudiante: ")
    
    estudiante_encontrado.nombre = nombre
    estudiante_encontrado.curso = curso
    estudiante_encontrado.carrera = carrera
    
    print("¡Estudiante actualizado exitosamente!")
    print()
    menu_crud_estudiantes()

def eliminar_estudiante():
    print()
    print('-------------- Eliminar Estudiante ---------------')
    try:
        carnet = int(input("Ingresa el carnet del estudiante que deseas eliminar: "))
    except ValueError:
        print("Error: El carnet debe ser un número entero.")
        print()
        menu_crud_estudiantes()
    
    estudiante_encontrado = None
    
    for estudiante in estudiantes:
        if estudiante.carnet == carnet:
            estudiante_encontrado = estudiante
            break

    if estudiante_encontrado is None:
        print("Error: No se encontró un estudiante con el carnet ingresado.")
        print()
        menu_crud_estudiantes()

    estudiantes.remove(estudiante_encontrado)
    print("¡Estudiante eliminado exitosamente!")
    print()
    menu_crud_estudiantes()

if __name__ == "__main__":
    main()