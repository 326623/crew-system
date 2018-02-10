ROUTE=/vagrant
#DIR=$ROUTE/crew-system
DIR=$ROUTE
PIP_SETUP=$DIR/crew_api
DB=$PIP_SETUP/database

# disable interactive prompt
export DEBIAN_FRONTEND=noninteractive
# prepare database password
#echo "mysql-server mysql-server/root_password password" | debconf-set-selections
#echo "mysql-server mysql-server/root_password_again password" | debconf-set-selections

apt-get update
# notive that it will prompt for password
apt install -y python3 python3-pip language-pack-zh-hans mysql-server

mysql < $DB/crew-user.sql
# preparing flask restplus
pip3 install --upgrade pip
pip3 install -r $PIP_SETUP/requirements.txt
pip3 uninstall crew_api
pip3 install -e $PIP_SETUP

# setting envvar
echo 'export FLASK_APP=crew_api' >> /home/vagrant/.bashrc
echo 'export FLASK_DEBUG=1' >> /home/vagrant/.bashrc

# moving mysql test database for testing acceleration
service mysql stop
ln -s /run/test /var/lib/mysql/test/
service mysql start

# if ! [ -L /var/www ]; then
#     rm -rf /var/www
#     ln -fs /vagrant /var/www
# fi
