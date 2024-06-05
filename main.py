from usuario import Usuario
from profesor import Profesor
from estudiante import Estudiante

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
        else:
            print("Opción inválida. Inténtalo de nuevo")

#Menú profesores            
def menu_crud_profesores():
    print("----------------- Menú Profesores -----------------")
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
        main()
    else:
        print("Opción inválida. Inténtalo de nuevo")

def crear_profesor():
    pass

def leer_profesores():
    pass

def actualizar_profesor():
    pass

def eliminar_profesor():
    pass

#Menú Estudiantes
def menu_crud_estudiantes():
    print("----------------- Menú Estudiantes -----------------")
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
        main()
    else:
        print("Opción inválida. Inténtalo de nuevo")

def crear_estudiante():
    pass

def leer_estudiantes():
    pass

def actualizar_estudiante():
    pass

def eliminar_estudiante():
    pass

if __name__ == "__main__":
    main()