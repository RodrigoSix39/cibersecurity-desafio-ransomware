import os
import pyaes
location = os.getcwd()  # Pega o diretório atual

for file in os.listdir(location): #Pega todos os arquivos dentro do diretório
    try:
        if file.endswith(".ransomwaretroll"): #Separa apenas os arquivos terminados em .ransomwaretroll
            print ("ransomwaretroll file found:\t", file)
            file_opn = open(file, "rb")
            file_data = file_opn.read()
            file_opn.close()

            ## chave para descriptografia
            key = b"testeransomwares"
            aes = pyaes.AESModeOfOperationCTR(key)
            decrypt_data = aes.decrypt(file_data)

            ## remover o arquivo criptografado
            os.remove(location+'/'+file)

            ## criar o arquivo descriptografado        
            new_file = open(f'{file.replace(".ransomwaretroll", "")}', "wb")
            new_file.write(decrypt_data)
            new_file.close()

    except Exception as e:
        raise e
        print ("Nenhum arquivo encontrado!")

print("Arquivos decriptados com sucesso!")