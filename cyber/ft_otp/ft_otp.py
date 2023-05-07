#!/home/luis/anaconda3/envs/42AI-lcasado-/bin/python

#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python

import os
import sys
import argparse
import OpenSSL
import rsa
import pprint
import warnings as _warnings
from cryptography.fernet import Fernet     # to cyfer Key into ft_otp.key
import base64

def create_argument_parser():

    def correct_length(file):
        """
          helper function checks if Hexadecimal key is longer than 64
        """
        # 1.- check if key exist
        cwd = os.getcwd()
        pathfile = os.path.join(cwd, file)
        if os.path.isfile(pathfile):
            # 2.- check if i can read the key 
            if os.access(pathfile, os.R_OK):
                # 3.- read the file and check length
                with open(pathfile, 'rb') as f:
                    text = f.read().strip()  # remove \n: does not belong to Key
                # 4.- if length is ok
                size = len(text)
                if  size >=64:
                    # 5.- if ti is a hexadecimal string.
                    is_hex = True
                    hex_chars = b'0123456789ABCDEF'
                    for char in text.upper():                     
                        if char not in hex_chars:
                            is_hex = False
                            break
                    del text
                    if is_hex:
                        return pathfile
                    else:
                        parser.error("Key is not hexadecimal")
                else:
                    parser.error(f"Key lenght of {size} is smaller than 64")
            else:
                parser.error(f"Can not read {pathfile}")
        else:
            parser.error(f"File {pathfile} does not exist")

    def correct_filename(argument):
        """
          helper function that recursion level passed at command line
        """
        if argument is None:
            parser.error(f"Missing file name '{argument}'")
        else:
            try:
                cwd = os.getcwd()
                filepath = os.path.join(cwd, argument)
                if os.path.isfile(filepath):
                    if not os.access(filepath, os.R_OK):
                        parser.error(f"can not read'{argument}'")
                    else:
                        return filepath
            except:
                parser.error(f"Can not find '{argument}'")
    msg = """
    Permet d’enregistrer un mot de passe initial, et qui est capable"
    de générer un nouveau mot de passe chaque fois qu’il est demandé"""
    parser = argparse.ArgumentParser(
                                     prog='Time One-Time-Password generator',
                                     description=msg,
                                     epilog='Este es el final de la ayuda',
                                     usage = "ft_otp -g key.hex | ./ft_otp -k ft_otp.key")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument( '-k',
                        help=f'I need a file ft_otp.key, qui sera crypté.',
                        type=correct_filename)
                        #nargs='+')
    group.add_argument('-g',
                        help='Clave hexadecimal de mas de 64 caracters',
                        type=correct_length
                        )
    group.add_argument('--GUI',
                        help='Ejecuta la aplicacion con un interface grafico',
                        action='store_true'
                        )


    return parser

def hotp(file):
    pass

def encrypt_key(path_to_key):
    path_file = os.path.split(path_to_key)
    path = path_file[0]

    # get the key i will use to seed cifer tool
    cwd = os.getcwd()
    cifer_key_path = os.path.join(os.environ["HOME"], ".ssh/.encrypt.key" )
    try:

        print("cifer_key_path", cifer_key_path)
        with open(cifer_key_path, 'rb') as f:
            cifer_key = f.read()
        print("cifer_key          = ", cifer_key)
        
        # initialize encrypter wiht the key 
        fernet = Fernet(cifer_key)

        # get the key i have to save into ft_otp.key cyphered#
        with open(path_to_key, 'rb') as f:
            totp_key_to_encrypt = f.read().strip()
        print("totp key           = ",totp_key_to_encrypt)

        
        totp_key_encrypted = fernet.encrypt(totp_key_to_encrypt)


        print("totp_key_encrypted = ",totp_key_encrypted)

        # write into ft_otp.key the cyphered#"
        with open(os.path.join(path, "ft_otp.key"), 'bw') as f:
            f.write(totp_key_encrypted)
        msg = "ft_otp.Key has been created"
        _warnings.warn(msg,RuntimeWarning, 2)
    except FileNotFoundError:
        msg = "Encription Key not found. Execute 'generate_encrypt_key.py'"
        _warnings.warn(msg,RuntimeWarning, 2)

def decrypt_key(path_to_key):
    path_file = os.path.split(path_to_key)
    path = path_file[0]

    # read the key used to seed cifer tool
    cifer_key_path = os.path.join(os.environ["HOME"], ".ssh/.encrypt.key" )
    with open(cifer_key_path, 'rb') as f:
            cifer_key = f.read()
    print("cifer_key          = ", cifer_key)

       
    # initialize encrypter wiht the key
    fernet = Fernet(cifer_key)

    # read TOTP encrypted key
    with open(path_to_key, 'br') as f:
        totp_key_encrypted = f.read()
    
    # decrypt TOTP Key
    key_cyphered = fernet.decrypt(totp_key_encrypted)
    print("key_cyphered       = ",key_cyphered)

    return key_cyphered


    
if __name__ == "__main__":
    parser = create_argument_parser()
    
    #args = parser.parse_args(sys.argv[1:])
    args = parser.parse_args(['-g','ft_otp.hex'])
    #args = parser.parse_args(['-k','ft_otp.key'])
    print("Estos son mis argumentos ",args)
    if args.GUI:
        _warnings.warn("Me han pedido qie me ejecute en modo grafico")
    else:
        if args.g is not None:
            msg = f"Me han dado una clave {args.g} para que la guarde "
            msg = msg + "cifrada en ft_otp.key"
            _warnings.warn(msg, RuntimeWarning, 2)
            encrypt_key(args.g)
        if args.k is not None:
           msg = "Me han dado pedido el proximo OTP basado "
           msg = msg + f"en {args.k}"
           totp_key = decrypt_key(args.k)
           _warnings.warn(msg, RuntimeWarning, 2)
    """
    #args = parser.parse_args(['-g', 'pepe'])
    print (args.g)
    version = OpenSSL.SSL.OpenSSL_version(OpenSSL.SSL.OPENSSL_VERSION)
    pprint.pprint(version)
    encript_key(args.g)
    """
    