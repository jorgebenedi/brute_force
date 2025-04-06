import hashlib
import sys

def md5(palabra, lista):
    for i in lista:
        # Importante encodear la palabra
        cifrado = i.encode('utf-8')
        # Lo hasheamos en MD5 (convertirlo a cifrado)
        encrypted = hashlib.md5(cifrado)
        # Si la palabra coincide con la palabra encryptada
        if palabra == encrypted.hexdigest():
            print(f"Se descifró la palabra: {i}")
            break


def sha1(palabra, lista):
    for i in lista:
        cifrado = i.encode('utf-8')
        encrypted = hashlib.sha1(cifrado)
        # una comparación entre el hash que hemos introducido y las palabras hasheadas de passwd.
        # Cuando el hash es identico muestra la palabra, porque hola por ejemplo ,siempre va a tener el mismo hash.
        # print(encrypted.hexdigest())
        # print("---")
        if palabra == encrypted.hexdigest():
            print(f"Se descifró la palabra: {i}")
            break


def sha256(palabra, lista):
    for i in lista:
        cifrado = i.encode('utf-8')
        encrypted = hashlib.sha256(cifrado)
        if palabra == encrypted.hexdigest():
            print(f"Se descifró la palabra: {i}")
            break


def sha512(palabra, lista):
    for i in lista:
        cifrado = i.encode('utf-8')
        encrypted = hashlib.sha512(cifrado)
        if palabra == encrypted.hexdigest():
            print(f"Se descifró la palabra: {i}")
            break


def main():
    print("..WELCOME TO PASSWORD GUESSER")
    print("Este programa solo descifra MD5 - SHA1 - SHA256 - SHA512")
    palabra = input()

    print("Identificando el método de ciframiento")

    with open("wordlist.txt","r", encoding="utf-8") as file:
        batch_size = 1000  # Tamaño del lote de líneas a procesar
        batch = []  # Almacenar líneas del lote

        for line in file:
            batch.append(line.strip())

            if len(batch) >= batch_size:
                if len(palabra) == 32:
                    md5(palabra, batch)
                elif len(palabra) == 40:
                    sha1(palabra, batch)
                elif len(palabra) == 64:
                    sha256(palabra, batch)
                elif len(palabra) == 128:
                    sha512(palabra, batch)
                else:
                    print("No contamos con ese método de ciframiento")
                batch = []

        # Procesar las líneas restantes en el último lote
        if batch:
            if len(palabra) == 32:
                md5(palabra, batch)
            elif len(palabra) == 40:
                sha1(palabra, batch)
            elif len(palabra) == 64:
                sha256(palabra, batch)
            elif len(palabra) == 128:
                sha512(palabra, batch)
            else:
                print("No contamos con ese método de ciframiento")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()





