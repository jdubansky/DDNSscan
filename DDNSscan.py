import socket
from multiprocessing import Pool
import time
import argparse



def scan(arg):
    target_ip, port = arg

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((target_ip, port))
        sock.close()

        return port, True
    except (socket.timeout, socket.error):
        return port, False


def showtest(arg):
    target_ip, port = arg
    time.sleep(port)
    return port, True

def main():
    parser = argparse.ArgumentParser(description='script port scan dynamic DNS servers given a list of hostnames')

    parser.add_argument('-v', '--verbose',
        action="store_true",
        help="verbose output" )

    parser.add_argument('-f',
        type=argparse.FileType('r'),
        help="file containing hostnames")

    args = parser.parse_args()

    if args.f is not None:
        print(args.f)
        with open(args.f) as hostsfile:
            print hostsfile.readline()


if __name__ == '__main__':
    main()
