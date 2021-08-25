sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx_1_9_11.conf
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/django.conf.py ask.wsgi:application