#!/Users/lcasado-/miniconda3/envs/42AI-stockholm/bin/python
#!/home/luis/anaconda3/envs/42AI-stockholm/bin/python

import os

def read_wannacry_extensions():
    """
    copied a file from 
    https://gist.github.com/xpn/facb5692980c14df272b16a4ee6a29d5
    
    this funcion reads from a file and adds into a set, 
    all file extensions affected by wanacry Ransommware.
    """
    try:
        filename = "wannacry_file_extensions.txt"
        pathfile = os.path.join(os.getcwd(), filename)
        ext = set()
        with open(pathfile, 'r') as f:
            for line in f:
                data = f.readline().strip()
                ext.add(data.lower())
        return sorted(ext)
    except FileNotFoundError:
        print(f"Not found file {filename} in cwd")

    
def recursive_walk(folderpath):
    global counter
    for root, dirs, files in os.walk(folderpath, topdown=True):
        # first treat files in folders

        for file in files:
            file_name, file_ext = os.path.splitext(file)
            # does file have an extension affected by Wannacry
            if file_ext in extensions:
                # rename all with ".ft" but the files ending with ".ft"
                if file_ext == ".ft":
                    fileout = file
                else:
                    fileout = file + ".ft"
            

                with open(os.path.join(root, file), 'rb') as infile: 
                    with open(os.path.join(root, fileout), 'wb') as outfile:
                        pass
                #try:

                #if os.access(os.path.join(root, file), os.R_OK):
                print(root, file)
                counter = counter + 1
        # second, if there are subfolders, treat them
        if len(dirs)>0:
            for dir in dirs:
                recursive_walk(os.path.join(root,dir))

if __name__ == "__main__":
    extensions = read_wannacry_extensions()
    print(extensions)
    home = os.environ['HOME']
    folderpath = os.path.join(home, "infection")
    counter = 0
    recursive_walk(folderpath)


            
    print(f"{counter} files treated")
