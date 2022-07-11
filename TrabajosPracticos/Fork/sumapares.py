import os
import argparse

parser = argparse.ArgumentParser(description='Process generator')
parser.add_argument('-n','--numero', type=int,
                    help='an integer for the accumulator', required=True)
parser.add_argument('--verbose','-v', action='store_true',
                    help='mode extended text')

args = parser.parse_args()

for i in range(args.numero):
    pid = os.fork()
    if pid == 0:
        if args.verbose:
            print(f'Starting process {os.getpid()}')
        result = 0
        for j in range(os.getpid()):
            if j % 2 == 0:
                result = result + j
        print(f'{os.getpid()}-{os.getppid()}:{result}')
        os._exit(0)
    hpid, status = os.wait()
    if (status == 0 and args.verbose):
        print("Ending process",hpid)


