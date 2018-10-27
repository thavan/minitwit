cd /var/www/minitwit.thavanathan.com
git pull --all
source prodenv.sh
#pkill -9 uwsgi
uwsgi muwsgi.ini
