#declarar
bandas=[]

print("***Altavoz es tu voz***:")
print("************************")
# Menú principal
opcion=100
while (opcion!=5):
    print("\n*** Menú Principal ***")
    print("1. Registrar banda")
    print("2.Buscar Informacion de una Banda")
    print("3.Agenda del Evento")
    print("4.Modificar una banda")
    print("5.Salir")

    opcion=int(input("digita una opcion:  "))

    if opcion==1:
        banda={}
        #creando datos del diccionario que se llama banda
        #tengo datos, para que no sobre escriba lo limpio
        banda["id"]=int(input("Digitael Id:   "))
        banda["nombre"]=input("Nombre de la Banda:   ")
        banda["genero"]=input("Genero:   ")
        banda["clasificacion"]=input("Clasificacion:   ")
        banda["tiempo"]=int(input("Tiempo:   "))
        banda["costo"]=int(input("Costo:   $"))
       #agregando un diccionario a una lista
        #aqui le digo a las lista envie las bandas, append es agregar
        bandas.append(banda)

    elif opcion==2:
        bandaBuscada=input("digita el nombre de la banda que buscas:  ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]==bandaBuscada:
                #como lo encontre muestro los datos de la banda
                print(f"id: {bandAuxiliar["id"]}--- nombre: {bandAuxiliar["nombre"]}")
            else:
                print("parce siga buscando...")
        pass
    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass