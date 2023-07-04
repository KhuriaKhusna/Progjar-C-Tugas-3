import sys
import socket
import logging
from multiprocessing import Process

def kirim_data(nama="kosong"):
    logging.warning(f"proses: {nama}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"(proses: {nama}) [CLIENT] sending {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        respon = "JAM HH:MM:SS\r\n"
        amount_received = 0
        amount_expected = len(respon)
        while amount_received < amount_expected:
            data = sock.recv(32).decode('utf-8')
            amount_received += len(data)
            logging.warning(f"(proses: {nama}) [DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning(f"(proses: {nama}) closing")
        sock.close()
    return


if __name__=='__main__':
    proses = []
    for i in range(10):
        p = Process(target=kirim_data, args=(i,))
        proses.append(p)
        
    for j in proses:
        j.start()
        
    for j in proses:
        j.join()
