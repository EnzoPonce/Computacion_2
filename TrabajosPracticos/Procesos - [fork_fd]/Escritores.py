import argparse as ap
import os
import time
import string
    
parser = ap.ArgumentParser(description="Procesos escritores en archivo")

parser.add_argument("-n",
                    "--number",
                    type=int,
                    required=True,
                    help="Numero de procesos a crear")
parser.add_argument("-r",
                    "--repeat",
                    type=int,
                    required=True,
                    help="Cantidad de veces a repetir")
parser.add_argument("-f",
                    "--file",
                    type=str,
                    required=True,
                    help="Ubicacion del archivo a escribir")
parser.add_argument("-v",
                    "--verbose",
                    help="Activar salida con mensajes",
                    action="store_true")
args = parser.parse_args()

with open(args.file, 'w+') as writer:
    alphabet = list(string.ascii_uppercase)
    for i in range(args.number):
        pid = os.fork()
        if pid == 0:
            for j in range(args.repeat):
                if args.verbose:
                    print(f"Proceso {os.getpid()} escribiendo letra '{alphabet[i]}'")
                writer.write(alphabet[i])
                writer.flush()
                time.sleep(1)
            os._exit(0)
   
    os.wait()
    writer.close()

with open(args.file, 'r') as file:
    text = file.readlines()
    print(''.join(text))
    file.close()    


