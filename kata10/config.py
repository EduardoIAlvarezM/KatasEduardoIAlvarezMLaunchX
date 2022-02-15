#def main():
#    try:
#        configuration=open('config.txt')
#    except FileNotFoundError:
#        print("No se pudo encontrar el archivo config.txt")
#if __name__ == '__main__':
#    main()

#def main():
#    try:
#        configuration=open('config.txt')
#    except Exception:
#        print("No se puede encontrar el archivo config.txt")

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Nose pudo encontrar el archivo config.txt")
    except IsADirectoryError:
        print("Archivo config.txt encotnrado pero es un directorio, no se puede leer el archivo")