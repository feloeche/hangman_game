import os
import random
import re

clear = lambda: os.system ("clear")

def chose_word(lista):
    number = random.randint(1, 5)
    word = lista[number]

    return word


def spaces(word):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',    
                't', 'u', 'v', 'x', 'y', 'z']
    guiones = word
    for i in letras:
        for x in word:
            if i == x:
                guiones = guiones.replace(x, "_")
    print(guiones)
    convertir= list(guiones)
    condition = True
    while condition:
        
        letra = input("INgrese una letra: ")
        cont = 0
    
        for i in word:
            
            
            if i == letra:
                
                
                convertir[cont] = letra
            else:        
                cont = cont + 1        
        cambio = "".join(convertir)
        print(cambio)  
        if word == cambio:
            condition = False

    
    
    
    
    clear()
def run():
    lista = ['hola', 'tres', 'cuantro', 'carro', 'avion']
    print("Adivina la plabra!!")


    word = chose_word(lista)
    print(word)
    size = spaces(word)



if __name__ == '__main__':
    run()