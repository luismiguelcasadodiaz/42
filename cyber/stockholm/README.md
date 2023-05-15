1. Download from https://gist.github.com/xpn/facb5692980c14df272b16a4ee6a29d5
   the file containing all file extensions affected by WannaCry Randsonware
2. Name such file as 'wannacry_file_extensions.txt'

3. Execute generate_encrypt_key.py
   It generates a symmetrical encryption key wiht Fernet.generate_key.
   This key is saved in ~/.ssh/.encrypt.key"

   I selected a symmetrical encryption key because requires less resources
   for encryption.

4. Execute stockholm.py
   Pequeño programa de cifrado. Es un ejercicio del bootcamp de ciberseguridad de
   42 Barcelona. Solamente afecta a los archivos de la carpeta
   '/Users/lcasado-/infection'

   usage:
        ./stockholm [-h] [-v] [-s] [-r] KEY

      optional arguments:
      -h, --help            show this help message and exit
      -v, --version         Muestra la versión del programa
      -s, --silent          No mostrar nombres de ficheros cifrados
      -r KEY, --reverse KEY
                              introduzca la clave para revertir el cifrado

   Recorre al árbol de archivos y directorios que hay en ~/infection.
   para ello se ayuda de os.walk. Por defecto no sigue los enlaces simbólicos

   

   Antes de iniciar el reverse verifica que la KEY introducida por el usuario
   coincide con la que se ha usado para el cifrado y que está guardada en:
   ~/.ssh/.encrypt.key

