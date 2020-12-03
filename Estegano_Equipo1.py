#Paquetes importados.
import cv2
class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

"""--------------------------------------------------------------------------------------------------"""
#Función para la opción 1.
def insertext():
    #Variables con el ancho y el alto de la imagen.
    anchura = obtenerimg('proyimag1T.png').shape[1]
    altura = obtenerimg('proyimag1T.png').shape[0]

    print(color.BOLD + "\t\tOPCIÓN: Insertar mensaje oculto en una imagen" + color.END)
    print()

    print(color.BOLD + f"proyimag1T.png tiene de ancho {anchura} y de alto {altura}." + color.END)
    print()

    #Muestra la imagen sin texto oculto.
    cv2.imshow('Imagen original', obtenerimg('proyimag1T.png'))
    cv2.waitKey(0)

    #Pide el mensaje que se desea guardar.
    mensaje = input(color.BOLD + "Introduzca el mensaje de texto a ocultar: " + color.END)
    print()

    print(color.BOLD + "Insertando el texto en la imagen..." + color.END)
    print()

    #Función para ocultar el texto en la imagen guardada en una variable.
    ocultar = textocult("proyimag1T.png", mensaje)

    #Guarda la imagen con el texto oculto.
    cv2.imwrite("proyimod1T.png", ocultar)

    #Variables con las imagenes con y sin texto oculto.
    original = cv2.imread("proyimag1T.png")
    estegano = cv2.imread("proyimod1T.png")

    #Coprobación de si las imagenes son iguales o no.
    if original.shape == estegano.shape: #Se ejecuta si el ancho, el alto y el canal de las imagenes coninciden.

        #Resta el ancho, el alto y los canales de las dos imagenes y los guarda en una variable.
        diferencia = cv2.subtract(original, estegano)

        #Guarda en tres variables distintas los resultados de la resta anterior.
        b, g, r = cv2.split(diferencia)

        #Se ejecuta si los resultados de las restas son 0.
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print(color.BOLD + f"El fichero proyimag1T.png es igual a proyimod1T.png" + color.END)
            print()

        # Se ejecuta si los resultados de las restas no son 0.
        else:
            print(color.BOLD + f"El fichero proyimag1T.png es diferente a proyimod1T.png" + color.END)
            print()

    # Se ejecuta si el ancho, el alto y el canal de las imagenes no coninciden.
    else:
        print(color.BOLD + "Tienen tamaño distinto." + color.END)
        print()

    #Muestra la imagen con el texto ya oculto.
    cv2.imshow('Con texto oculto', estegano)
    cv2.waitKey(0)

"""--------------------------------------------------------------------------------------------------"""
#Función para ocultar el texto en la imagen.
def textocult(imagen, mensaje):
    #Variable para llamar a la función que lee la imagen.
    imagen = obtenerimg("proyimag1T.png")

    #Variable con el mensaje en UNICODE.
    mensgene = gencode(mensaje)

    #Cambia los bit de la imagen para ocultar el mensaje.
    for i in range(len(imagen)):
        for j in range(len(imagen[0])):
            try:
                imagen[i][j][0] = next(mensgene)
            except StopIteration:
                imagen[i][j][0] = 0
        return imagen

"""--------------------------------------------------------------------------------------------------"""
#Función para la opción 2.
def extractext():
    print(color.BOLD + "\t\tOPCIÓN: Extraer mensaje oculto en una imagen" + color.END)
    print()

    print("El fichero de la imagen con texto oculto se llama: proyimod1T.png")
    print()

    print("Extrayendo el texto de la imagen...")
    print()

    print("El texto oculto es:", (desocultext("proyimod1T.png")))

"""--------------------------------------------------------------------------------------------------"""
#Función para extraer el texto de la imagen.
def desocultext(imagen):
    # Variable para llamar a la función que lee la imagen.
    imagen = obtenerimg("proyimod1T.png")

    #Variable vacia para insertar el mensaje extraido de la imagen.
    mensaje = ''

    #Lee bit a bit para encontrar el mensaje oculto.
    for i in range(len(imagen)):
        for j in range(len(imagen[0])):
            if imagen[i][j][0] != 0:
                mensaje = mensaje + chr(imagen[i][j][0])
            else:
                return mensaje

"""--------------------------------------------------------------------------------------------------"""
#Función para la opción 3.
def gris():
    print(color.BOLD + 'OPCIÓN: Convertir la imagen a escala de grises' + color.END)
    print()
    print('El fichero de la imagen con texto oculto se llama: proyimod1T.png')
    print()
    print('Convirtiendo la imagen a escala de grises...')

    #Lee la imagen.
    ima = "proyimag1T.png"
    imagen = cv2.imread(ima, 0)

    # Guarda la imagen en escala de grises.
    cv2.imwrite("proyimgr1T.jpg", 0)

    # Muestra la imagen en escala de grises.
    cv2.imshow("Escala de grises", imagen)
    cv2.waitKey(0)

"""--------------------------------------------------------------------------------------------------"""
#Función para leer la imagen.
def obtenerimg(imagen):
    imagen = cv2.imread(imagen, cv2.IMREAD_UNCHANGED)
    return imagen

"""--------------------------------------------------------------------------------------------------"""
#Función para transformar el mensaje en UNICODE.
def gencode(mensaje):
    for code in mensaje:
        yield ord(code)

"""--------------------------------------------------------------------------------------------------"""

#Programa.
while True:
    print()
    #Menú de opciones.
    print("\t\t\tAPLICACIÓN ESTEGANO")
    print("\t\t1) Insertar mensaje oculto en una imagen")
    print("\t\t2) Extraer mensaje oculto en una imagen")
    print("\t\t3) Convertir la imagen a escala de grises")
    print("\t\t4) Salir")

    print()
    opcion = int(input("\t\tOpción: ")) #Input para elegir la opción.
    print()

    #Varios if para llamar a las funciones según la opción elegida.
    if opcion == 1: #Opción para ocultar el texto en la imagen.
        insertext()

    elif opcion == 2: #Opción para sacar el texto oculto de la imagen.
        extractext()

    elif opcion == 3: #Opción para convertir y mostrar la imagen en escala de grises.
        gris()

    elif opcion == 4: #Opción para cerrar el programa.
        break #Rompe el bucle para salir del programa.

    else:
        print("Esa opción no está en el menú. Por favor elija otra.")