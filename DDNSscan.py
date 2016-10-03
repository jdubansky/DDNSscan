import socket

from multiprocessing import Pool

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

if __name__ == '__main__':
    target_ip = raw_input('Target IP: ')
    num_procs = int(raw_input('Number of processes: '))

    ports = range(1, 1025)
    pool = Pool(processes=num_procs)

    for port, status in pool.imap_unordered(scan, [(target_ip, port) for port in ports]):
        print port, 'is', 'open' if status else 'closed'
