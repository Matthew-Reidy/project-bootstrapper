
import subprocess
import os
import sys 

def run() -> None:
    try:
        if len(sys.argv) > 3:
            print("Only 3 arguments allowed!")

        specifiedDir: str = sys.argv[1]
        os.mkdir(specifiedDir)
        os.chdir(specifiedDir)
        subprocess.run(args=["git init -b main"], shell=True)
        subprocess.run(args=f"git remote add origin {sys.argv[2]}", shell=True)
        info = subprocess.run(args=["git remote -v"], shell=True, capture_output=True, text=True)
        print(info)

        with open(".gitignore", "w") as gitignore:
            gitignore.write("# ignored files go in here \n __pycache__")

        with open("README.MD", "w" ) as readme:
            readme.write("# Hello, World!")

        subprocess.run(args=["git add ."], shell=True)
        subprocess.run(args=['git commit -m "First Commit"'], shell=True)
        subprocess.run(args=["git push origin main"], shell=True)
    except IndexError:
        print("missing arguments!")

    


run()

