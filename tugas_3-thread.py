import sys
import socket
import logging
import threading

def kirim_data(nama="kosong"):
    logging.warning(f"nama thread: {nama}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"(thread: {nama}) [CLIENT] sending {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        respon = "JAM HH:MM:SS\r\n"
        amount_received = 0
        amount_expected = len(respon)
        while amount_received < amount_expected:
            data = sock.recv(32).decode('utf-8')
            amount_received += len(data)
            logging.warning(f"(thread: {nama}) [DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning(f"(thread: {nama}) closing")
        sock.close()
    return


if __name__=='__main__':
    threads = []
    for i in range(4):
        t = threading.Thread(target=kirim_data, args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()
