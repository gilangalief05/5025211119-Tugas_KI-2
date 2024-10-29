import socket
import threading
import DES

username = input("Input your username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5555


def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "name":
                client.send(username.encode("utf-8"))
            else:
                if message == "":
                    client.close()
                    break
                message_dec = DES.decrypt_str(message)
                print(message_dec)
                # print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        try:
            message = f"{username}: {input("")}"
            message_enc = DES.encrypt_str(message)
            client.send(message_enc.encode("utf-8"))
            # client.send(message.encode("utf-8"))
        except:
            print("An error occured!")
            client.close()
            break

try:
    client.connect((host, port))
except:
    client.close()
else:
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()