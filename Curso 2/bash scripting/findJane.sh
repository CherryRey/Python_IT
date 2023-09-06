
#!/bin/bash

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

for file in $files; do
  if test -e ~/data/$file; then
    echo $file >> oldFiles.txt;
  fi
done



####
#!/bin/bash
>oldFiles.txt
files=$(grep " jane " /home/student-00-fc6190c0ca66/data/list.txt | cut -d ' ' -f 3)

for file in $files; do
  if test -e ~/$file; then
    echo $file >> oldFiles.txt;
  else
    echo "File doesn't exist";fi
done

