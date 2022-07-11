import sys
import getopt

def main():

    list = sys.argv[1:]
    try:
        opts,args = getopt.getopt(list,'o:m:n:')
    except getopt.GetoptError:
        sys.exit()


    for i, j in opts:
        if i == "-o":
            try:
                if j in '+-*/':
                    arg = j
            except TypeError:
                print("Ingrese un argumento valido")

        if i == '-m':
            try:
                n1 = int(j)
            except ValueError:
                print("Ingrese un numero entero por favor")
                exit()

        if i == '-n':
            try:
                n2 = int(j)
            except ValueError:
                print("Ingrese un numero entero por favor")
                exit()

    if arg == '+':
        return print(n1+n2)
    elif arg == '-':
        return print(n1-n2)
    elif arg == '*':
        return print(n1*n2)
    else:
        return print(n1/n2)


main()
