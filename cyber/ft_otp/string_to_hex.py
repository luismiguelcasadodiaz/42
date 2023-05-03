#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python
import sys
import os

def string_to_hex(texto):
    #print(f"texto  :{texto}")
    texto_b = texto.encode('utf-8')
    #print(f"texto b: {texto_b}")
    texto_h = texto_b.hex()
    #print(f"texto h: {texto_h}")
    return texto_h
     
if __name__ == "__main__":
    num_args = len(sys.argv[1:])
    if num_args == 2:
        texto = sys.argv[1]
        size = len(texto)
        if size >= 32:
            cwd = os.getcwd()
            filepath = os.path.join(cwd, sys.argv[2])
            if os.path.isfile(filepath):
                print(f" File {filepath}, exists")
                sys.exit(-1)
            else:
                text = string_to_hex(texto)
                with open(filepath,'wb') as f:
                    f.write(text.encode('utf-8'))
                sys.exit(0)
        else:
            print(f"Waiting for at least 32 chars. {texto} has only {size}")
        
    else:
            print("Usage : string_to_hex [text] [file_to_save]")