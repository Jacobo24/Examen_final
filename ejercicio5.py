def encryptRailFence(text, key):
    # Crear una matriz para el texto cifrado
    # clave de texto sin formato = filas
    # tamaño(texto) = columnas
    # Espacio para los huecos en blanco
    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        # Mirar la dirección de la fila
        # invertir la dirección si acabamos de introducir
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        # llenar el alfabeto correspondiente
        rail[row][col] = text[i]
        col += 1
        # encuentra la primera fila
        
        if dir_down:
            row += 1
        else:
            row -= 1
    # usando la matriz rail
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
    # encontrar la dirección
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        # encuentra la siguiente columna
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
    # lee la matriz
    # el texto resultante
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        # mirar la dirreccion
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        # coloco el marcador
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
if __name__ == "__main__":
    print(encryptRailFence("defend the east wall", 3))