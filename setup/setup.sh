#!/bin/bash
clear
#if [ -z "$1" ]
#then
#    echo "Empty path!"
#	exit 1
#else
#    echo "Good day, I start to setup project in $1"
echo $PWD
exit 1
alpha="This is a test string in which the word \"test\" is replaced."
beta="${alpha//test/$1}"
echo ${beta} > mshop.ini
exit 1
sudo apt-get install uwsgi nginx uwsgi-plugin-python
sudo ln -s $1/setup/nginx/mshop.conf /etc/nginx/sites-enabled/
sudo ln -s $1/config/uwsgi/mshop.ini /etc/uwsgi/apps-enabled/
#sudo service nginx restart
#sudo service uwsgi restart

fi