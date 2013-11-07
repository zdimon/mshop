#!/bin/bash
clear
if [ -z "$1" ]
then
    echo "Empty name of the project!"
	exit 1
else
    echo -e "Good day, I start to setup project $1 \n"

echo -e "Install virtualenv.......\n"
sudo apt-get install python-virtualenv


echo -e "Install pip git.......\n"
sudo apt-get install python-pip
sudo apt-get install git
sudo apt-get install libpq-dev
sudo apt-get install python-dev
sudo apt-get install libfreetype6-dev

sudo apt-get install libjpeg-dev
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib


echo -e "Init virtual environment .......\n"
virtualenv $1_ve

cd ./$1_ve
echo -e "Go to env dir: $PWD\n"



echo -e "Get project from git .......\n"
git clone https://github.com/zdimon/mshop.git

echo -e "Go to project directory .......\n"
cd ./mshop



alpha="server { \n
    listen      80; \n
    server_name $1.local; \n
    access_log  /var/log/nginx/$1.log;\n
    location / {\n
           uwsgi_pass      unix:///tmp/$1.sock;\n
            include         uwsgi_params;\n
            client_max_body_size 200M;\n
    }\n
    location /static {\n
        alias $PWD/static/;\n
    }\n
}"

a=`dirname $PWD`


echo -e "Writing nginx ini file......."
echo -e ${alpha} > $1.conf


alpha="[uwsgi] \n
thread          = 3    \n
master          = true\n
processes       = 2\n
module          = settings.wsgi\n
chdir           = $PWD\n
socket          = /tmp/$1.sock\n
logto           = /var/log/uwsgi/$1.log\n
vacuum          = true\n
max-requests    = 5000\n
buffer-size     = 32768\n
chmod-socket    = 777\n
plugins         = python\n
home            = ${a}\n
"



echo -e "Writing uwsgi ini file.......\n"
echo -e ${alpha} > $1.ini


echo -e "Installing uwsgi nginx .......\n"
sudo apt-get install uwsgi nginx uwsgi-plugin-python


echo -e "Making simlink on nginx conf file.......\n"
sudo ln -s $PWD/$1.conf /etc/nginx/sites-enabled/

echo -e "Making simlink on uwsgi ini file.......\n"
sudo ln -s $PWD/$1.ini /etc/uwsgi/apps-enabled/

echo -e "Restarting.......\n"
sudo service nginx restart
sudo service uwsgi restart

echo -e "Edit database connection in settings.py.......\n"
pause

echo -e "Going to environment.......\n"
source ../bin/activate

echo -e "Setup django and requirement packets.......\n"
pip install -r requirements.txt

read -p "Please edit $PWD/setings/setings.py and set connection to your database. Then press any key to continue... " -n1 -s


echo -e "Make static dir.......\n"
mkdir static
chmod 775 static

echo -e "Collect static .......\n"
python manage.py collectstatic --noinput


echo -e "Run syncdb command.......\n"
python manage.py syncdb

echo -e "Run migrate command.......\n"
python manage.py migrate

echo -e "On localhost Add this string in /etc/host '127.0.0.1   $1.local' and then you can access to site by using this address http://$1.local \n"
read -p "Press any key to continue... " -n1 -s
fi