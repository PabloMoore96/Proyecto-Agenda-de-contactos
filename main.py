import funcagenda

if __name__=="__main__": #Acá para dar uso al main, llamé a la función desde el otro archivo, y armé el menú  usando un while, que corra el programa
    option_menu = 0      # mientras que el valor de la opción sea diferente de 5
    while(option_menu != 5):
        print('\n1 Agregar contacto \n2 Mostrar contacto \n3 Buscar contacto \n4 Eliminar contacto \n5 Salir\n')
        op = input("Seleccionar opcion del menu \n")
        if (op.isdigit()): #Aca cree una excepción, similar a las que suelo hacer para que no rompa el programa si la opción introducida no es un número
            option_menu = int(op) #Acá le pedi al usuario que seleccióne la opción que necesite, y cada opción corre una función
            if(option_menu == 1):
                funcagenda.add_contact()
            elif(option_menu == 2):
                funcagenda.show_contact()
            elif(option_menu == 3):
                funcagenda.search_contact()
            elif(option_menu == 4):
                funcagenda.delete_contact()
            elif(option_menu > 5 or option_menu < 1): #Esta opción está por si el usuario pone una opción numérica distinta de las solicitadas en el menú
                print("Elegir una opcion valida")
            else: #Opción == 5, rompe el bucle
                print("Gracias por usar el programa.")
