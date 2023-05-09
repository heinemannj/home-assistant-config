#!/bin/sh
#
# .gitpushupdates.sh
#
# cd /config
# git init
#
# git config user.email "heinemannj66@gmail.com"
# git config user.name "heinemannj"
#
# mkdir .ssh
# ssh-keygen -t rsa -b 4096 -C "heinemannj66@gmail.com"
# git config core.sshCommand "ssh -i /config/.ssh/id_rsa -F /dev/null"
#
# git add .
# git commit -m "Initial commit"
#
# git branch -M master
# git remote add origin git@github.com:heinemannj/home-assistant-config.git
#
# git push -u origin master
#
cd /config
git add .
git commit -m "config files on `date +'%d-%m-%Y %H:%M:%S'`"
git push -u origin master
