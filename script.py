
import subprocess
import os
import sys 

def run() ->None:
    if len(sys.argv) > 3:
        print("Only 3 arguments allowed!")
    try:

        specifiedDir: str = sys.argv[1]
        os.mkdir(specifiedDir)
        os.chdir(specifiedDir)
        subprocess.run()
        with open(".gitignore", "w") as gitignore:
            gitignore.write("# ignored files go in here")

    except IndexError:
        print("not enough arguments")


    
        
run()