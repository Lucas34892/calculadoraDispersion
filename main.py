while True:
    try:
        #Declarar variables
        datosCorrectos = False
        sumaPromedio = 0
        sumaMedia = 0
        sumaVarianza = 0
        datos = []
        datosVarianza = []
        #Seleccion de tipo de dato
        print("Tipos de datos disponibles:")
        print("1. Datos en tabla")
        print("2. Datos sueltos")
        tipoTabla = int(input("Ingrese la tabla que elegira: "))
        if(tipoTabla == 1):
            #Declarar variables
            marcaIntervalo = []
            frecuencia = []
            frecuenciaAcumulada = 0
            cantidadIntervalos = int(input("Ingrese la cantidad de intervalos: "))
            #Obtener los datos
            for i in range(1, cantidadIntervalos + 1):
                print()
                minimoIntervalo = float(input(f"Ingrese la inicial del intervalo {i}: "))
                maximoIntervalo = float(input(f"Ingrese la final del intervalo {i}: "))
                frecuencia.append(float(input("Ingrese la frecuencia de este dato: ")))
                marcaIntervalo.append((maximoIntervalo + minimoIntervalo) / 2)
            #Promedio
            for i in range(0, cantidadIntervalos):
                frecuenciaAcumulada += frecuencia[i]
                sumaPromedio += marcaIntervalo[i] * frecuencia[i]
            promedio = sumaPromedio / frecuenciaAcumulada
            #DesviacionMedia
            for i in range(0, cantidadIntervalos):
                sumaMedia += ((abs(marcaIntervalo[i] - promedio)) * frecuencia[i])
            desviacionMedia = sumaMedia / frecuenciaAcumulada
            #Varianza
            for i in range(0, cantidadIntervalos):
                sumaVarianza += ((marcaIntervalo[i] - promedio)* frecuencia[i]) ** 2
            varianza = sumaVarianza / frecuenciaAcumulada
            #Desviacion estandar
            desviacionEstandar = varianza ** (1/2)
            #Imprimir las respuestas
            print()
            print(f"El  promedio es {promedio}.")
            print()
            print(f"La desviacion media es {desviacionMedia}.")
            print()
            print(f"La varianza es {varianza}.")
            print()
            print(f"La desviacion estandar es {desviacionEstandar}.")
            print()
        elif(tipoTabla == 2):
            cantidadDatos = int(input("Ingrese la cantidad de datos: "))
            print()
            #Obtener los datos
            for i in range(1, cantidadDatos + 1):
                datos.append(float(input(f"Ingrese el dato {i}: ")))
            #Verificar los datos
            while (datosCorrectos == False):
                print()
                print("Estos son los datos:")
                print(datos)
                correctos = input("Estan correctos los datos(Si o no): ").lower()
                if(correctos == "si"):
                    datosCorrectos = True
                else:
                    print()
                    cambiarDato = int(input("Ingrese el número de dato que quiera cambiar(Número): "))
                    datos[cambiarDato - 1] = float(input("Ingrese el dato nuevo: "))
            #Promedio
            for i in range(0, cantidadDatos):
                sumaPromedio += datos[i]
            promedio = sumaPromedio / cantidadDatos
            #Desviacion Media
            for i in range(0, cantidadDatos):
                sumaMedia += (abs(datos[i] - promedio))
            desviacionMedia = sumaMedia / cantidadDatos
            #Varianza
            for i in range(0, cantidadDatos):
                sumaVarianza += (datos[i] - promedio) ** 2
            varianza = sumaVarianza / cantidadDatos
            #Desviacion estandar
            desviacionEstandar = varianza ** (1/2)
            #Imprimir las respuestas
            print()
            print(f"El  promedio es {promedio}.")
            print()
            print(f"La desviacion media es {desviacionMedia}.")
            print()
            print(f"La varianza es {varianza}.")
            print()
            print(f"La desviacion estandar es {desviacionEstandar}.")
            print()
    except Exception as e:
        print()
        print(f"Parece que ha ocurrido el siguiente error {e}.")
        print()