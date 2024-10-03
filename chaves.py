import rsa
import os
size = input("Digite o tamanho da chave: ")
end = os.getcwd() + '/kyes'
counter = 1
original_end = end

while os.path.exists(end):
    end = f"{original_end}_{counter}"
    counter += 1

os.makedirs(end)

public_key, private_key = rsa.newkeys(int(size))

##crio o arquivo pub
public = end + '/Pub.txt'
#codifico o exponente e modulo da chave para o formate PEM
arq = open(public,'w')
arq.write(str(public_key._save_pkcs1_pem()))
arq.close()

##crio o arquivo pri
private = end + '/Pri.txt' 
arq = open(private,'w')

##codifico o exponente e modulo da chave para o formate PEM
arq.write(str(private_key._save_pkcs1_pem()))
arq.close()

print('Chaves geradas com sucesso')
print(public)
print(private)