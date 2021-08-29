sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
python ask/manage.py loadtestdata qa.Question:20 qa.Answer:50
python ask/manage.py makemigrations qa
python ask/manage.py migrate