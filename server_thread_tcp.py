#Servidor TCP
import socket
from threading import Thread

global tcp_con
import rsa

# A chave publica da pessoa para quem vou enviar a mensagem
arqnomepub = 'C:\\Users\\Willian\\Downloads\\branquinho-main\\branquinho-main\\kyes\\zago\\chaveschavePub.txt'
arq = open(arqnomepub,'rb')
# Carrega o conteúdo do arquivo
txt = arq.read()
arq.close()

# Carrega a chave pública do parceiro no formato PEM
pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')

# Caminho para a minha chave privada
arqnomepri = 'C:\\Users\\Willian\\Downloads\\branquinho-main\\branquinho-main\\kyes\\Pri.txt'
arq1 = open(arqnomepri,'rb')
txt1 = arq1.read()
arq1.close()

# Carrega minha chave privada no formato PEM
pri = rsa.PrivateKey.load_pkcs1(txt1, format='PEM') 
        
def enviar():
    global tcp_con
    print ('Para sair use CTRL+X\n')
    msg = input()
    while msg != '\x18':
        mensagem_codificada = msg.encode('utf-8')
        msgEncriptada = rsa.encrypt(mensagem_codificada,pub)
        tcp_con.send(msgEncriptada)
        msg = input()
    tcp_con.close()
        

# Endereco IP do Servidor
HOST = ''

# Porta que o Servidor vai escutar
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

t_env = Thread(target=enviar, args=())
t_env.start()

while True:
    print('Servidor online')
    tcp_con, cliente = tcp.accept()
    print ('Concetado por ', cliente)

    while True:        
        msg = tcp_con.recv(512)
        if not msg: break
        msgd = rsa.decrypt(msg, pri)
        msgd = msgd.decode()
        print("Zago:",msgd)
        
    print ('Finalizando conexao com Zago', cliente)
    tcp_con.close()