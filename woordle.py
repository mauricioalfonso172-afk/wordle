#### VARIABLES GLOBALES

intentos = 0
#palabra_usuario = input("Escriba su palabra:")
palabra_secreta = "perro"
letras_verificadas = []
palabras_verificadas = []
cantidad_letras = 5

def verificar_palabra(palabra_usuario, palabra_secreta):

    letras_verificadas = []

    for letra in range(cantidad_letras):
        
        palabras_iguales = palabra_usuario[letra] == palabra_secreta[letra]
        letra_en_palabra_secreta = palabra_usuario[letra] in palabra_secreta

        if palabras_iguales:
            letras_verificadas.append(f"[{palabra_usuario[letra]}]")
        elif letra_en_palabra_secreta:
            letras_verificadas.append(f"({palabra_usuario[letra]})")
        else:
            letras_verificadas.append(f"{palabra_usuario[letra]}")

    return palabras_verificadas.append(letras_verificadas)

def conteo_de_intentos(attemps):
    
    while attemps <= 5:

        palabra_usuario = input("Escriba su palabra:")
        verificar_palabra(palabra_usuario, palabra_secreta)
        
        if palabra_usuario == palabra_secreta:
            for i in palabras_verificadas:
                print(i)
            #print(palabras_verificadas)
            print("Fin del juego")
            break

        else:
            for i in palabras_verificadas:
                print(i)
            #print(palabras_verificadas)
            attemps = attemps + 1
            print(f"Le quedan {5 - attemps} intentos")

conteo_de_intentos(intentos)