#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python

import os
import sys
import argparse
import OpenSSL
import pprint

def create_argument_parser():

    def correct_length(file):
        """
          helper function that if Hexadecimal key is longer than 64
        """
        # 1.- check if key exist
        cwd = os.getcwd()
        pathfile = os.path.join(cwd, file)
        if os.path.isfile(pathfile):
            # 2.- check if i ca read the key 
            if os.access(pathfile, os.R_OK):
                # 3.- read the file and check length
                with open(pathfile, 'rb') as f:
                    text = f.read()
                # 4.- if length is ok y return the key
                if len(text) >=64:
                    del text
                    return pathfile
                else:
                    parser.error("Key smaller than 64")
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

   
    parser.add_argument('--GUI',
                        help='Ejecuta la aplicacion con un interface grafico',
                        type=correct_length
                        )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument( '-k',
                        help=f'I need a file ft_otp.key, qui sera crypté.',
                        type=correct_filename)
                        #nargs='+')
    group.add_argument('-g',
                        help='Clave hexadecimal de mas de 64 caracters',
                        type=correct_length
                        )


    return parser

def hotp(file):
    pass

def encript_key(path_to_key):
    
    os.chdir(os.environ["HOME"])
    cwd = os.getcwd()
    print(cwd)
    pub_key_path = os.path.join(cwd, ".ssh/alice_public.pem" )
    print(pub_key_path)
    with open(pub_key_path, 'rb') as f:
        pubkey = f.read()
    PKey = OpenSSL.crypto.load_publickey(OpenSSL.SSL.FILETYPE_PEM, pubkey)
    resutl = PKey.encrypt(b"hello")
    print(PKey)
    
if __name__ == "__main__":
    parser = create_argument_parser()
    print("Estos son mis argumentos ",sys.argv)
    args = parser.parse_args(sys.argv[1:])
    #args = parser.parse_args(['-g', 'pepe'])
    print (args.g)
    version = OpenSSL.SSL.OpenSSL_version(OpenSSL.SSL.OPENSSL_VERSION)
    pprint.pprint(version)
    encript_key(args.g)
    