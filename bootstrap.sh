#!/bin/bash

if [ -z "$1" ]; then
    echo "must include the directory of your new project!"
    exit 1
fi

mkdir $1 

cd $1

git init -b main 

touch .gitignore

touch README.MD

printf "#ignored files" >> .gitignore

printf "# hello, world!" >> README.MD

if [ -n "$2" ]; then 

    git remote add origin $2 

    git remote -v

    git add .

    git commit -m "first commit"

    git push -u origin main

fi


