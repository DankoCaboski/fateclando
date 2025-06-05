#Cliente TCP
import socket
import rsa
from threading import Thread

global tcp_con

# Endereço das chaves publicas e provadas
sereverPubKey = "C:\\Users\\Antonio Zago\\Desktop\\Fatec\\Banco de dados distribuidos\\criptografia-masterchavePub.txt"
sereverPriKey = "C:\\Users\\Antonio Zago\\Desktop\\Fatec\\Banco de dados distribuidos\\criptografia-masterchavePri.txt"
arq = open(sereverPubKey,'rb')
txt = arq.read()
arq.close()

#Abre o arquivo da chave publica
with open(sereverPubKey, 'rb') as f:
    chave_publica_data = f.read()
    public_key = rsa.PublicKey.load_pkcs1(chave_publica_data, format='PEM')

#Abre o arquivo da chave privada
with open(sereverPriKey, 'rb') as t:
    chave_privada_data = t.read()
    private_key = rsa.PrivateKey.load_pkcs1(chave_privada_data, format='PEM')

#Função para receber as mensagens enviadas pelo servidor
def receber():
    global tcp_con
    while True:
        msg = tcp_con.recv(512)
        msgd = rsa.decrypt(msg, private_key) #Encripta a msg com a minha chave privada
        print ("Server:",msgd.decode())

# Função de envio
def enviar():
    global tcp_con
    print ('Para sair use CTRL+X\n')
    msg = input()
    while msg != '\x18':
        mensagem_codificada = msg.encode('utf-8') 
        msgEncriptada = rsa.encrypt(mensagem_codificada,public_key) # decodifica a msg com a chave publica do Danko
        tcp_con.send(msgEncriptada)
        msg = input()
    tcp_con.close()
    
# Endereco IP do Servidor (maquina do Danko) 
SERVER = '192.168.137.115'

# Porta que o Servidor esta escutando
PORT = 5002

tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp_con.connect(dest)


t_rec = Thread(target=receber, args=())
t_rec.start()

t_env = Thread(target=enviar, args=())
t_env.start()