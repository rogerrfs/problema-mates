#!/usr/bin/env python3

def find_line(num):
        
    # Número
    n = 1
    # Línea
    l = 1
    # Números per línea
    npl = 1

    # Crear un bucle while
    i = 1
    while i != 0:
        
        # Augmentar el número de línea
        l += 1
        # Augmentar el número de números per línea
        npl += 1
        
        # Buscar si el número escollit està a la línea
        for i in range(npl):
            # Si el número està es trenca el bucle
            if n == num:
                i = 0
            # Si no, es continua buscant el número
            else:
                n += 1
                
    # Retornar el número de línea
    return f"{l}\n"


while True:
    
    print("Selecciona un número ('q' per tancar, 'info' per mostrar la informació del programa)")
    input_num = input(">> ")
    
    if input_num == 'q':
        print("\nBye!")
        quit()
        
    elif input_num == 'info':
        print(
    """
Hola
    """
        )
    
    else:
        i_n = int(input_num)

        print(find_line(i_n))


