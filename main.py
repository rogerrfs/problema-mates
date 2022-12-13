#!/usr/bin/env python3

def main_text():
    return """
 _   _                    _____              
| \ | | _   _  _ __ ___  |_   _| _ __   __ _ 
|  \| || | | || '_ ` _ \   | |  | '__| / _` |
| |\  || |_| || | | | | |  | |  | |   | (_| |
|_| \_| \__,_||_| |_| |_|  |_|  |_|    \__, |
                                       |___/ 
                       
                        |---------------------|
                        | Fet per Roger Fibla |
                        |---------------------|

Aquest programa és per trobar en quina fila es
trobaria un nombre selecionat posicionat en un
triangle.

\033[1;3mhttps://github.com/rogerrfs/problema-mates\033[0m
    """
    
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

def main():
    while True:
        
        print("Selecciona un número ('q' per tancar, 'info' per mostrar la informació del programa)")
        input_num = input(">> ")
        
        if input_num == 'q':
            print("\Adéu!")
            quit()
            
        elif input_num == 'info':
            print(main_text())
        
        elif input_num == "":
            quit()
            
        else:
            i_n = int(input_num)

            if i_n <= 0:
                quit()
                
            else:
                print(f"El nombre {i_n} es troba a la línea: {find_line(i_n)}")

#################################################################################
#################################################################################


if __name__ == "__main__":
    main()
