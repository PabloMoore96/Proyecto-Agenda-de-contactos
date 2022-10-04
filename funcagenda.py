# Proponer una solucion que simule una agenda de contactos haciendo uso de diccionarios.
# Para el diccionario las llaves seran los nombres de los contactos y como valor estará una tupla que contenga el número telefónico y el correo electrónico.
# Se tendrá un menú con las siguientes opciones: 1 Agregar contacto, 2 mostrar contactos, 3 buscar contacto, 4 eliminar contacto, 5 salir.
# Su propuesta deberá utilizar minimamente: Constantes y/o variables, cond selectivos, multiples, bucles, diccionarios y tuplas, uso de funciones y main.



agenda = {}

def add_contact():
    # Agregar un contacto a la agenda
    nombre=input("Ingrese nombre de contacto: \n")
    tel=input("Ingrese su número de teléfono: \n")
    while not tel.isnumeric():
        tel=input("Ingrese su número de teléfono correctamente: \n")
    tel=int(tel)
    correo=input("Ingrese su email: \n")
    agenda.update({nombre: (tel, correo)})

    return agenda


def show_contact():

    for key, values in agenda.items():
        print(f"Nombre: {key} \nTelefono: {values[0]} \nEmail: {values[1]}")
        print("")
    # Mostrar todos los contactos en la agenda   

def search_contact():
    nom=input("Ingresar nombre a buscar: \n") #Declaro esta variable para utilizarla como una referencia a la key del diccionario.
    for key, values in agenda.items():
        if (nom == key): #Si la variale nom es igual al valor de una, kay, la mostrará en pantalla.
            print(f"Nombre: {key} \nTelefono: {values[0]} \nEmail: {values[1]}")
            print("")

def delete_contact():
    for key, values in agenda.items():
        print(f"Nombre: {key} \nTelefono: {values[0]} \nEmail: {values[1]}")
        print("")
    nom=input("Ingresar contacto a eliminar: \n") #Usé la misma base que en mostrar contacto, pero acá declare la variable nom, y en este caso
    if (nom == key):                              # la condicioné para que si es igual a key, elimine el string de "nom"
        agenda.pop(nom)

