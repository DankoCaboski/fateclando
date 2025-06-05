import rsa
import os
size = input("Digite o tamanho da chave: ")
end = os.getcwd() + '/kyes'
counter = 1
original_end = end

if os.path.exists(end):
    os.remove(end + '/pub.txt')
    os.remove(end + '/pri.txt')
else:
    os.makedirs(end)

public_key, private_key = rsa.newkeys(int(size))

## crio o arquivo pub
public = end + '/pub.txt'
arq = open(public,'w')
## codifico o exponente e modulo da chave para o formate PEM
arq.write(str(public_key._save_pkcs1_pem()))
arq.close()

## crio o arquivo pri
private = end + '/pri.txt' 
arq = open(private,'w')
## codifico o exponente e modulo da chave para o formate PEM
arq.write(str(private_key._save_pkcs1_pem()))
arq.close()

print('Chaves geradas com sucesso')