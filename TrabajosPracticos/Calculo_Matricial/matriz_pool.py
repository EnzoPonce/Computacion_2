import argparse
import os
from multiprocessing import Pool

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f",
                        "--file",
                        type=str,
                        required=False,
                        help="file")
    parser.add_argument("-p",
                        "--process",
                        type=int,
                        required=True,
                        help="Number of process")
    parser.add_argument("-c",
                        "--calculate",
                        type=str,
                        required=False,
                        help="Operation")
    args = parser.parse_args()
    pool = Pool(processes=args.process)
    results = pool.map(funcion_calculo, openFile(args.file))
    print("padre %d, hijo %d"% (os.getpid(),os.getppid()),results)

def openFile(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            return list(line.strip().replace(",","").replace(" ", ""))

def funcion_calculo(x):
    
    var = [int(x)*int(x) for i in (x)]
    return var

if __name__ == '__main__':
    main()