
import time
import socket

def lcg(s, a, c, m):
  return int(int(s*a+c) % m)

HOST = "0.0.0.0"
PORT = 65430

a = int((time.time() * 723)) % 100000000
c = int((time.time() * 123)) % 100000000
m = int((time.time() * 534)) % 100000000

flag = "flag{1cg_is_4s_safe_as_p0ssib13}".encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  while True:
    conn, addr = s.accept()
    with conn:
      s0 = int((time.time() * 903)) % 100000000
      conn.sendall("1 - get random numbers\n2 - predict next random number\n".encode())
      while True:
        data = conn.recv(1024)
        if not data:
          break
        if (str(data)[2] == "1"):
          s_arr = ""
          for _ in range(10):
            s0 = lcg(s0, a, c, m)
            s_arr += str(s0) + " "
          conn.sendall(f"{s_arr}\n".encode())
          print(a, c, m)
        elif (str(data)[2] == "2"):
          s_next = lcg(s0, a, c, m)
          conn.sendall(f"{str(s0)}\n".encode())
          print(s_next)
          data = conn.recv(1024)
          if not data:
            break
          if (int(data.decode()) == s_next):
            conn.sendall(flag)
          else:
            conn.sendall("wrong\n".encode())
        else:
          conn.sendall("1 or 2\n".encode())
        break