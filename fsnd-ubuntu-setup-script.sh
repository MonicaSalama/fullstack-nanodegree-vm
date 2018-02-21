# Make sure you run this script as the user you use everyday on your machine

# Update the Ubuntu package database
sudo apt-get -qqy update

# Install Python 3 and Python 3 packages
sudo apt-get -qqy install make zip unzip postgresql
sudo apt-get -qqy install python3 python3-pip
sudo -H pip3 install --upgrade pip
sudo -H pip3 install flask packaging oauth2client redis passlib flask-httpauth
sudo -H pip3 install sqlalchemy flask-sqlalchemy psycopg2 bleach requests

# Install Python 2 and Python 2 packages
sudo apt-get -qqy install python python-pip
sudo -H pip2 install --upgrade pip
sudo -H pip2 install flask packaging oauth2client redis passlib flask-httpauth
sudo -H pip2 install sqlalchemy flask-sqlalchemy psycopg2 bleach requests

# Make sure that PostgreSQL is running
sudo service postgresql start

# Create a PostgreSQL user for the current Linux user
sudo -u postgres createuser -dRS $USER
createdb

# Create forum database
createdb forum

# Create the vagrant PostgreSQL user
echo "#######################################################################################"
echo "# Creating the vagrant PostgreSQL user. Set password to \"vagrant\" (without quotes)... #"
echo "#######################################################################################"
sudo -u postgres createuser -dRSP vagrant

# Create the news database and have it owned by the vagrant PostgreSQL user
sudo -u postgres createdb -O vagrant news

# Run the forum database setup. Assumes this script is in the root of the extracted zip file
psql forum -f ./vagrant/forum/forum.sql

# Download and install the Redis software
cd $HOME
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
sudo make install
