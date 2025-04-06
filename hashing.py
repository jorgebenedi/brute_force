import hashlib
import sys


def md5(palabra):
    encrypted = hashlib.md5(palabra)
    # Para que se muestre en hexadecimal.
    print(encrypted.hexdigest())
    # Siempre se mostrarán 32 caracteres en MD5.


def sha1(palabra):
    encrypted = hashlib.sha1(palabra)
    print(encrypted.hexdigest())


def sha256(palabra):
    encrypted = hashlib.sha256(palabra)
    print(encrypted.hexdigest())


def sha512(palabra):
    encrypted = hashlib.sha512(palabra)
    print(encrypted.hexdigest())


def main():
    print(".:Cifrador")
    print("Elige el método de ciframiento")
    print("1-MD5\n2-SHA1\n3-SHA256\n4-SHA512\n#-Salir")

    modo = input("Introduce el tipo de ciframiento: ")

    palabra = input("Introduce la palabra a cifrar: ")
    palabra = palabra.encode('utf-8')
    print("-" * 50)

    if modo == "1":
        md5(palabra)
    elif modo == "2":
        sha1(palabra)
    elif modo == "3":
        sha256(palabra)
    elif modo == "4":
        sha512(palabra)
    else:
        sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
