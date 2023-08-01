
import subprocess
import os
import sys 

def run() -> None:
    if len(sys.argv) > 3:
        print("Only 3 arguments allowed!")

 

    specifiedDir: str = sys.argv[1]
    os.mkdir(specifiedDir)
    os.chdir(specifiedDir)
    subprocess.run(args="git init -b main")
    subprocess.run(args=f"git remote add origin {sys.argv[2]}")
    with open(".gitignore", "w") as gitignore:
        gitignore.write("# ignored files go in here \n __pycache__")
    with open("README.MD", "w" ) as readme:
        readme.write("# Hello, World!")
    subprocess.run(args="git add .")
    subprocess.run(args='git commit -m "First Commit"')
    subprocess.run(args="git push origin main")

    


run()